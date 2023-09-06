import  configparser
import os
proDir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(proDir,'config.ini')

class ReadConfig:
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)

    def get_base_url(self):
        protocol = self.cf.get('HTTP','protocol')
        #测试环境
        # ip = self.cf.get('HTTP','ip')
        # port= self.cf.get('HTTP','port')
        # base_url=protocol + '://' + ip + ':' + port
        # print(base_url)
        #其他类型地址
        basics=self.cf.get("HTTP",'basics')
        base_url=protocol + '://' + basics
        return base_url

    def get_email(self,mail_key):
        email_value=self.cf.get('EMAIL',mail_key)
        return email_value

if __name__ == '__main__':
    ReadConfig().get_base_url()

