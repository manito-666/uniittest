import os
import unittest
import json
from common.httpSet import HttpMethod
from common.myLog import MyLog
from common.readTestData import ReadTestData
from config.readConfig import ReadConfig
from common.operateExcel import OperateExcle

proDir=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
excelPath = os.path.join(proDir, "testData","test.xlsx")

class MessageTest(unittest.TestCase):
    def setUp(self):
        self.data = ReadTestData()
        self.http = HttpMethod()
        self.config = ReadConfig()
        self.log=MyLog
        self.ope=OperateExcle()
        self.log.info(message="----------测试开始----------", name="test03_Message.py")

    def tearDown(self):
        self.log.info(message="----------测试结束----------", name="test03_Message.py")

    def test_message(self):
        '''
        验证会员发送消息功能
        '''
        max_row = self.ope.count_case('message', excelPath)
        for i in range(max_row-1):
            testdata=self.data.read(["message"])
            method = testdata[i][4]
            headers = testdata[i][5]
            url = self.config.get_base_url() + testdata[i][6]
            data = testdata[i][7]
            exp = testdata[i][8]
            self.http.request_log(method, url, data, headers=headers)
            status_code,res_json=self.http.http_method(method, url, data, headers)
            dict_json = json.loads(res_json)
            con=dict_json['data']['err_code']
            try:
                self.assertEqual(status_code, 200, msg=">>>接口请求失败")
                self.assertEqual(con, exp,msg=">>>断言失败，实际返回值是：%s" % con)
                self.log.info('测试通过')
                self.ope.write_data('message',i+2,10,con)
                self.ope.write_data('message', i+2, 11,'✅')
            except AssertionError as e:
                self.log.error('Assertion Error: %s' % e)
                self.ope.write_data('message', i + 2, 12, '❌')
                self.fail("测试失败")

