from app import app, db

# from flask import Flask, render_template, flash, redirect, url_for
# from app.forms import LoginForm
#
# from config import Config#从config模块导入Config类
#
# app = Flask(__name__)
#
# @app.route('/')
# @app.route('/index')
# def index():
# 	return render_template('index2.html')
from app.models import User, Post


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}


if __name__ == '__main__':
    # 通过url_map可以查看整个flask中的路由信息
    print(app.url_map)
    # 启动flask程序
    app.run(debug=True)
