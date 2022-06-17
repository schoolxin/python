# -*- coding:utf-8 -*-
# @FileName  :app.py
# @Time      :2022/6/16 15:24
# @Author    :dzz
# @Function  :
from flask import Flask
from flask import request, render_template

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route("/signin", methods=['GET'])
def signin_form():
    return render_template('form.html')


@app.route("/signin", methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == '123':
        return render_template('signin-ok.html',usernames=username)
    else:
        return render_template('form.html')


if __name__ == "__main__":
    app.run()
