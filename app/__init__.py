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
login = LoginManager(app)
login.login_view = 'login'  # 如果未登录用户尝试查看受保护的页面，Flask-Login将自动将用户重定向到登录表单

from app import routes, models  # 导入一个新模块models，它将定义数据库的结构，目前为止尚未编写
