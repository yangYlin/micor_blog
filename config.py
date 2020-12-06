import os

basedir = os.path.abspath(os.path.dirname(__file__))  # 获取当前.py文件的绝对路径


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you will never guess'
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'mysql:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/flask_micor_blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
