import logging
import os
from logging.handlers import RotatingFileHandler  # 日志处理

from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy  # 从包中导入类

from config import Config  # 从config模块导入Config类

app = Flask(__name__)
app.config.from_object(Config)
# print(app.config['SECRET_KEY'])

db = SQLAlchemy(app)  # 数据库对象
migrate = Migrate(app, db)  # 迁移引擎对象
login = LoginManager(app)  # 登录
login.login_view = 'login'  # 如果未登录用户尝试查看受保护的页面，Flask-Login将自动将用户重定向到登录表单

if not app.debug:
    # ...

    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240,
                                       backupCount=5)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup')

from app import routes, models, errors  # APP每增加一个模块，必需在init.py中添加才能访问
