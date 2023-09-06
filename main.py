import unittest
import os
import time
from BeautifulReport import BeautifulReport
from common.sendMail import sendmail
proDir = os.path.split(os.path.realpath(__file__))[0]
test_case_path = os.path.join(proDir, "test_case")
report_path=os.path.join(proDir,'report')


if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H.%M.%S", time.localtime(time.time()))
    report_title = '接口测试报告' + now + '.html'
    suite_tests = unittest.defaultTestLoader.discover(test_case_path, pattern="test*.py", top_level_dir=None)
    # "."表示当前目录，"*tests.py"匹配当前目录下所有test.py结尾的用例
    reportPath = report_path
    BeautifulReport(suite_tests).report(filename=report_title, description='全部用例测试', report_dir=reportPath,
                                        theme="theme_cyan")
    sendmail()

