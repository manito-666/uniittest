import json

from common.operateExcel import OperateExcle

from config.readConfig import ReadConfig
import os
proDir=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
excelPath = os.path.join(proDir, "testData","test.xlsx")

class ReadTestData:
    def __init__(self):
        self.open_excel=OperateExcle()
        self.set_excel=ReadConfig()

    #读取excel中的所有测试数据并添加到集合中
    def read(self,sheets):
        test_data=[]
        for sheet1 in sheets:
            max_row = self.open_excel.count_case(sheet1, excelPath)
            for case_id in range(1,max_row):
                testdata=self.open_excel.read_data_list(sheet1, case_id)
                test_data.append(testdata)
        return test_data





