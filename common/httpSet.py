import json
import requests
from common.myLog import MyLog

class HttpMethod:
    def __init__(self):
        self.log=MyLog()
    def get_method(self,url,data=None,headers=None):
        try:
            res=requests.get(url=url,params=data,headers=headers)
            status_code = res.status_code
            res_json = res.json()
            return status_code, res_json

        except Exception as e:
            self.log.error('Error:%s' %e)

    def post_method(self,url,data=None,headers=None):
        try:
            res=requests.post(url=url,data=data,headers=json.loads(headers))
            status_code=res.status_code
            res_json=res.json()
            return status_code,res_json

        except Exception as e:
            self.log.error('Error:%s' %e)

    def http_method(self, method, url, data=None, headers=None,**kwargs):
        if method == 'get':
            status_code, res_json=self.get_method(url,headers)
        elif method == 'post':
            status_code, res_json = self.post_method(url, data, headers)

        return status_code, json.dumps(res_json,ensure_ascii=False,sort_keys=False,indent=2)

    def request_log(self,method,url,data=None,files=None,headers=None, **kwargs):
        self.log.info("接口请求方式 ==>> {}".format(method))
        self.log.info("接口请求地址 ==>> {}".format(url))
        self.log.info("接口请求头 headers参数 ==>> {}".format(json.dumps(headers, ensure_ascii=False,sort_keys=False,indent=2)))
        # self.log.info("接口请求 params 参数 ==>> {}".format(json.dumps(data, ensure_ascii=False,sort_keys=False,indent=2)))
        self.log.info("接口请求体 data 参数 ==>> {}".format(data))
        