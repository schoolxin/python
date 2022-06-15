# -*- coding:utf-8 -*-
# @FileName  :stmpDemo01.py
# @Time      :2022/6/14 17:23
# @Author    :dzz
# @Function  :

import smtplib
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr


def _format_addr(s):
    name, addr = parseaddr(s)  # 使用<> 分割字符串
    return formataddr((Header(name, 'utf-8').encode(), addr))  # 因为如果包含中文，需要通过Header对象进行编码。


if __name__ == "__main__":
    server = smtplib.SMTP_SSL("smtp.mxhichina.com", 465)

    msg = MIMEMultipart()
    msg['From'] = _format_addr('Python爱好者 <%s>' % 'bi@orderplus.com')
    msg['To'] = _format_addr('管理员 <%s>' % "deng,dengzz")
    msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

    # 邮件正文是MIMEText:
    msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
                        '<p><img src="cid:0"></p>' +
                        '</body></html>', 'html', 'utf-8'))
    # 添加附件就是加上一个MIMEBase，从本地读取一个图片:
    with open('./test.png', 'rb') as f:
        # 设置附件的MIME和文件名，这里是png类型:
        mime = MIMEBase('image', 'png', filename='test.png')
        # 加上必要的头信息:
        mime.add_header('Content-Disposition', 'attachment', filename='test.png')
        # mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        # 把附件的内容读进来:
        mime.set_payload(f.read())
        # 用Base64编码:
        encoders.encode_base64(mime)
        # 添加到MIMEMultipart:
        msg.attach(mime)

    # server.set_debuglevel(1)

    server.login('bi@orderplus.com', 'Orderplus.2020')  # 用发件人邮箱和密码登陆smtp服务器

    server.sendmail('bi@orderplus.com', ['iraq.deng@orderplus.com'], msg.as_string())

    server.quit()
