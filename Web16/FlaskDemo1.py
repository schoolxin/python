# -*- coding:utf-8 -*-
# @FileName  :FlaskDemo1.py
# @Time      :2022/6/16 14:17
# @Author    :dzz
# @Function  :


from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return "<h1>hello</h1>"


@app.route("/signin", methods=['GET'])
def signin_form():
    return '''
        <form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>
    '''


@app.route("/signin", methods=['POST'])
def signin():
    # 从表单中获取数据
    data = request.get_data()

    print(data)

    return data


if __name__ == "__main__":
    app.run()
