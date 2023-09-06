# coding:utf-8
import smtplib
import time,sys,os
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from common.myLog import MyLog
from  config.readConfig import ReadConfig

# 测试报告的路径
proDir=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
Reportpath=os.path.join(proDir,'report')
logger = MyLog()
# 配置收发件人
r= ReadConfig()
receive = r.get_email("addr")
# 163的用户名和密码
send_name =r.get_email("name")
send_pwd = r.get_email("pwd")
subject=r.get_email('subject')
text=r.get_email('email_text')

def sendmail():
    #获取报告目录下最新的测试报告
    dirs = os.listdir(Reportpath)
    dirs.sort()
    newreportname = dirs[-1]
    logger.info('The new report name: {0}'.format(newreportname))
    # 创建一个带附件的邮件实例
    message=MIMEMultipart()
    # 邮件的其他属性
    message['From'] = send_name   #发送人
    message['Subject'] = Header(subject, 'utf8').encode()
    message['To'] = receive   #接收人
    # 邮件正文内容
    attr2 = MIMEText(text, 'plain', 'utf-8')
    message.attach(attr2)
    #构造附件
    path=os.path.join(Reportpath,newreportname)
    attr1=MIMEText(open(path,'rb').read(),'base64','utf-8')
    attr1["content_Type"]='application/octet-stream'
    attr1["Content-Disposition"] = 'attachment; filename="subject.html"'
    message.attach(attr1)
    try:
        server = smtplib.SMTP('smtp.163.com', 25)
        server.login(send_name, send_pwd)
        server.sendmail(send_name, receive,message.as_string())
        logger.info("发送邮件至 {}".format(receive))
        logger.info("发送邮件成功")
    except Exception as e:
        logger.error('失败：' + str(e))


if __name__ == '__main__':
    sendMail = sendmail()
