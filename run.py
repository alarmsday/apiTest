import pytest,os
from datetime import datetime

if __name__ == '__main__':
    alluredir = "/Users/liuhaoran/PycharmProjects/apiTest/report/" + str(datetime.now().strftime("%Y%m%d%H%M%S"))
    pytest.main(["-s", "/Users/liuhaoran/PycharmProjects/apiTest/testCase/", "-q", "--alluredir", alluredir])
    os.system("allure generate " + alluredir + " -o " + alluredir + "/allureReport")