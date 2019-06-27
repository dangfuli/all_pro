# coding=utf-8

import smtplib,time
from lib.getConfig import *
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

mail_info = getConfig(os.path.join(os.path.dirname(os.path.dirname(__file__)),'config/qqMail.json'))
# {
#   "from": "623037035@qq.com",
#   "password": "xspwqntmjvqwbcbd",
#   "to": "623037035@qq.com",
#   "title": "悦小说api",
#   "smtp": "smtp.qq.com"
# }

send_msg = '测试发送邮件'

def send_mail(send_file=None):
    # 带附件的实例
    qq_mail = MIMEMultipart()
    ## 基本信息
    qq_mail["From"] = Header(mail_info['from'],'utf-8')
    qq_mail['To'] = Header(mail_info['to'],'utf-8')
    qq_mail['Subject'] = Header(mail_info['title'],'utf-8')

    ## 添加邮件正文
    qq_mail.attach(MIMEText(send_msg,'plain','utf-8'))

    ## 附件
    if send_file is not None:
        ## 实例文本附件，发送
        fj = MIMEText(open(send_file,'rb').read(),'base64','utf-8')
        fj['Content-Type'] = 'application/octet-stream'
        fj['Content-Disposition'] = 'attachment; filename="{0}.html"'.format(time.strftime('%m_%d_%H_%M',time.localtime()))
        qq_mail.attach(fj)
    try:
        ## 配置发送的账号密码，发送邮件
        qqMail_obj = smtplib.SMTP_SSL(mail_info['smtp'],465)
        qqMail_obj.login(mail_info['from'],mail_info['password'])
        qqMail_obj.sendmail(mail_info['from'],mail_info['to'],qq_mail.as_string())
        print('邮件发送成功')
    except Exception as e:
        print('邮件发送出错：%s'% e)
if __name__ == '__main__':
    send_mail('../report/06-27-09-22.html')

