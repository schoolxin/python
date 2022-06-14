# -*- coding:utf-8 -*-
# @FileName  :stmpDemo01.py
# @Time      :2022/6/14 17:23
# @Author    :dzz
# @Function  :

import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr


def _format_addr(s):
    name, addr = parseaddr(s)  # 使用<> 分割字符串
    return formataddr((Header(name, 'utf-8').encode(), addr)) # 因为如果包含中文，需要通过Header对象进行编码。


if __name__ == "__main__":
    server = smtplib.SMTP_SSL("smtp.mxhichina.com", 465)

    msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
    msg['From'] = _format_addr('Python爱好者 <%s>' % 'bi@orderplus.com')
    msg['To'] = _format_addr('管理员 <%s>' % "deng,dengzz")
    msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

    # server.set_debuglevel(1)

    server.login('bi@orderplus.com', 'Orderplus.2020')  # 用发件人邮箱和密码登陆smtp服务器

    server.sendmail('bi@orderplus.com', ['iraq.deng@orderplus.com'], msg.as_string())

    server.quit()
