import common.configHttp as http
from common.Log import MyLog as Log
import json
import common.jsonTools as jsonTools

class SpuSave:
    def __init__(self):
        self.log = Log.get_log()
        self.jsonTool = jsonTools.jsonTools()
        self.logger = self.log.logger
        self.headers  = {"Content-Type": "application/json", "Authorization": "Bearer ed9e5fd5-dd4a-4dba-80d0-3f861523a561"}
        self.host = "http://java.goodscenter.mng.turboradio.cn"
        self.data = {"goodsType": "1", "goodsSubType": "11", "cateName": ["12815"], "cateId": "12815",
                    "goodsName": "刘昊然测试1592314435", "enName": None, "approvalNumber": "1592314435", "dosage": None,
                    "form": None, "manufacturer": None, "deleted": 0, "id": None, "attrs": None}

    def modifyParameter(self,key,value):
        self.jsonTool.modifyJson(self.data,key,value)

    def run(self):
        httpExcute = http.ConfigHttp();
        httpExcute.set_url(self.host+"/spu/save")
        httpExcute.set_headers(self.headers)
        httpExcute.set_data(json.dumps(self.data))
        res = httpExcute.get()
        self.logger.info(res.text)
        self.logger.info("spu上架执行完成")
        return res


if __name__ == '__main__':
    # test = SpuSave("http://java.goodscenter.mng.turboradio.cn/spu/save",
    #                {"Content-Type": "application/json", "Authorization": "Bearer ed9e5fd5-dd4a-4dba-80d0-3f861523a561"},
    #                {"goodsType": "1", "goodsSubType": "11", "cateName": ["12815"], "cateId": "12815",
    #                 "goodsName": "刘昊然测试1592314435", "enName": None, "approvalNumber": "1592314435", "dosage": None,
    #                 "form": None, "manufacturer": None, "deleted": 0, "id": None, "attrs": None})
    test = SpuSave();
    test.modifyParameter("approvalNumber","123124123")
    kk = json.loads(test.run().text)
    print(kk)
    ooo = jsonTools.jsonTools().getValue(kk,"error")
    print(ooo)


