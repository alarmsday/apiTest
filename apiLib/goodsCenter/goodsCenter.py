import common.configHttp as http
from common.Log import MyLog as Log
import json
import common.jsonTools as jsonTools

class SpuQuery:
    def __init__(self):
        self.log = Log.get_log()
        self.jsonTool = jsonTools.jsonTools()
        self.logger = self.log.logger
        self.headers  = {"Content-Type": "application/json", "Authorization": "Bearer ed9e5fd5-dd4a-4dba-80d0-3f861523a561"}
        self.host = "http://java.goodscenter.mng.turboradio.cn"
        self.path = ""
        self.params = {}
        self.data = {}

    #修改参数 0修改bodydata，1修改url后parmas
    def modifyJson(self,i,key,value):
        if i == 0:
            self.jsonTool.modifyJson(self.data,key,value)
        elif i == 1:
            self.jsonTool.modifyJson(self.params,key,value)
        else:
            self.logger.error("修改参数失败")

    #执行接口调用
    def run(self,method):
        httpExcute = http.ConfigHttp();
        httpExcute.set_url(self.host+self.path)
        httpExcute.set_headers(self.headers)
        httpExcute.set_data(json.dumps(self.data))
        httpExcute.set_params(self.params)
        if method == 0:
            res = httpExcute.get()
        if method == 1:
            res = httpExcute.post()
        self.logger.info(res.text)
        return res

    def spuSave(self):
        self.path = "/spu/save"
        self.data = {"goodsType": "1", "goodsSubType": "11", "cateName": ["12815"], "cateId": "12815",
                    "goodsName": "刘昊然测试1592314435", "enName": None, "approvalNumber": "1592314435", "dosage": None,
                    "form": None, "manufacturer": None, "deleted": 0, "id": None, "attrs": None}
        self.run(0)
        self.logger.info(self.path+"done"+"\tspu上架执行完成")

    def spuQuery(self):
        self.path = "/spu/query"
        self.data = {"pageNum":1,"pageSize":10}
        self.run(1)
        self.logger.info(self.path+"done"+"\tspu上架执行完成")

    def configSkuRegister(self):
        self.path = "/configsku/register"
        self.data = {"id":None,"spuId":"${spuId}","goodsName":"${goodsName}","goodsType":"1","goodsSubType":"11",
                     "title":"${title}","subTitle":None,"highlights":None,"externalCode":None,"barcode":None,
                     "specName":"硕大的","originTableId":None,"integral":None,"approvalNumber":"${approvalNumber}",
                     "originPrice":100,"stock":"23212","detailTitle":"APOE心脑血管风险基因检测",
                     "detailsCode":"51c181c3caf711e98cfc049226c12d63","merchantId":"578",
                     "merchantName":"产品测试","deliveryMerchantId":"578","deliveryMerchantName":"产品测试",
                     "settlementDiscountType":1,"settlementDiscount":None,"bundleItems":[],"buyLimitToList":[],"operator":"刘昊然"}
        self.run(1)
        self.logger.info(self.path + "done" + "\tspu上架执行完成")

if __name__ == '__main__':
    SpuQuery().spuQuery()


