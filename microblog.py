from app import app
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




if __name__ == '__main__':
    app.run(debug=True)