from datetime import datetime
from hashlib import md5

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):  # 混入类，有4个常用的字段
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')  # dynamic query,不做了查询操作，可以先做排序
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)

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
