from datetime import datetime
from hashlib import md5
from time import time

import jwt
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login, app


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


followers = db.Table(
    'followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),  # 自己的粉丝
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))  # 你关注人的ID
)


class User(UserMixin, db.Model):  # 混入类，有4个常用的字段
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')  # dynamic query,不做了查询操作，可以先做排序
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    followed = db.relationship(
        'User',  # 自引用
        secondary=followers,  # 关联表
        primaryjoin=(followers.c.follower_id == id),  # 粉丝ID
        secondaryjoin=(followers.c.followed_id == id),  # UP主
        backref=db.backref('followers', lazy='dynamic'),
        lazy='dynamic'
    )

    def __repr__(self):
        # return '<User {}>'.format(self.username)
        return '<User {}, Email {}, Password_Hash {}, Posts {}'.format(self.username, self.email, self.password_hash,
                                                                       self.posts)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    # 返回用户头像的URL，并缩放到请求的大小（以像素为单位）
    def avatar(self, size=8):
        digst = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digst, size)

    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)

    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)

    def is_following(self, user):
        return self.followed.filter(followers.c.followed_id == user.id).count() > 0
        # self.followed 自己关注的；    followers.c.followed_id == user.id   user关注的

    def followed_posts(self):
        followed = Post.query.join(followers, (followers.c.followed_id == Post.user_id)).filter(
            followers.c.follower_id == self.id)  # 我关注的人所以帖子
        own = Post.query.filter_by(user_id=self.id)  # 自己帖子
        return followed.union(own).order_by(Post.timestamp.desc())  # 2个UNION拼接

    # 得到加密后的参数
    def get_reset_password_token(self, expires_in=600):  # 超期时间，600s
        return jwt.encode(
            {'reset_password': self.id, 'exp': time() + expires_in},
            app.config['SECRET_KEY'], algorithm='HS256').encode('utf-8')

    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, app.config['SECRET_KEY'],
                            algorithms=['HS256'])['reset_password']
        except:
            return '密码被破坏'
        return User.query.get(id)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}'.format(self.body)


'''
数据库添加用户命令：
1） 添加wangsan
 from app import db
 from app import models        
 from app.models import User,Post
 
 u = User(username='wangsan', email='wangsan@example.com')
 u.set_password('123456')    
 u.check_password('123456')
 db.session.add(u)
 db.session.commit()
 


'''
