from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy  # 从包中导入类

from config import Config  # 从config模块导入Config类

app = Flask(__name__)
app.config.from_object(Config)
# print(app.config['SECRET_KEY'])

db = SQLAlchemy(app)  # 数据库对象
migrate = Migrate(app, db)  # 迁移引擎对象

from app import routes, models  # 导入一个新模块models，它将定义数据库的结构，目前为止尚未编写
