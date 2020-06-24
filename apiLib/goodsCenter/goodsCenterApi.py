import common.httpTools as http
from common.loggerHandler import MyLog as Log
import json
import common.jsonTools as jsonTools
from common.httpHandler import httpHandler

class spuSave(httpHandler):
    def __init__(self):
        self.host = "http://java.goodscenter.mng.turboradio.cn"
        self.headers = {"Content-Type": "application/json", "Authorization": "Bearer ed9e5fd5-dd4a-4dba-80d0-3f861523a561"}
        self.path = "/spu/save"
        self.params = None
        self.data = {"goodsType": "1", "goodsSubType": "11", "cateName": ["12815"], "cateId": "12815",
                     "goodsName": "刘昊然测试1592314435", "enName": None, "approvalNumber": "1592314435", "dosage": None,
                     "form": None, "manufacturer": None, "deleted": 0, "id": None, "attrs": None}

    def excute(self):
        self.response = self.run(0)
        self.logger.info(self.path + "done" + "\tspu上架执行完成")
        return self.response

class spuQuery(httpHandler):
    def __init__(self):
        self.host = "http://java.goodscenter.mng.turboradio.cn"
        self.headers = {"Content-Type": "application/json",
                        "Authorization": "Bearer ed9e5fd5-dd4a-4dba-80d0-3f861523a561"}
        self.path = "/spu/query"
        self.params = None
        self.data = {"pageNum":1,"pageSize":10}

    def excute(self):
        self.response = self.run(1)
        self.logger.info(self.path+"done"+"\tspu上架执行完成")
        return self.response

class configSkuRegister(httpHandler):
    def __int__(self):
        self.host = "http://java.goodscenter.mng.turboradio.cn"
        self.headers = {"Content-Type": "application/json",
                        "Authorization": "Bearer ed9e5fd5-dd4a-4dba-80d0-3f861523a561"}
        self.path = "/configsku/register"
        self.params = None
        self.data = {"id": None, "spuId": "${spuId}", "goodsName": "${goodsName}", "goodsType": "1",
                     "goodsSubType": "11",
                     "title": "${title}", "subTitle": None, "highlights": None, "externalCode": None, "barcode": None,
                     "specName": "硕大的", "originTableId": None, "integral": None, "approvalNumber": "${approvalNumber}",
                     "originPrice": 100, "stock": "23212", "detailTitle": "APOE心脑血管风险基因检测",
                     "detailsCode": "51c181c3caf711e98cfc049226c12d63", "merchantId": "578",
                     "merchantName": "产品测试", "deliveryMerchantId": "578", "deliveryMerchantName": "产品测试",
                     "settlementDiscountType": 1, "settlementDiscount": None, "bundleItems": [], "buyLimitToList": [],
                     "operator": "刘昊然"}

    def excute(self):
        self.response = self.run(1)
        self.logger.info(self.path + "done" + "\tspu上架执行完成")
        return self.response

class configSkuChannels(httpHandler):
    def __init__(self):
        self.host = "http://java.goodscenter.mng.turboradio.cn"
        self.headers = {"Content-Type": "application/json",
                        "Authorization": "Bearer ed9e5fd5-dd4a-4dba-80d0-3f861523a561"}
        self.path = "/configsku/channels"
        self.params = None
        self.data = {"channelConfigs": [{"detailsCode": None, "priceState": 0, "salePrice": 100,
                                         "saleIntegral": None, "storeId": "105624", "storeName": "晓琳总店", "stock": None,
                                         "mergeStatus": None, "saleState": 0, "channel": "${channel}",
                                         "useDefaultDetail": 1, "integralState": 1, "stockState": 1,
                                         "itemPriceToList": [], "logTo": {"operator": "刘昊然"}}], "skuNo": "${skuNo}"}

    def excute(self):
        self.response = self.run(1)
        self.logger.info(self.path + "done" + "\t渠道上架执行完成")
        return self.response

class goodsQuerySku(httpHandler):
    def __init__(self):
        self.host = "http://java.goodscenter.mng.turboradio.cn"
        self.headers = {"Content-Type": "application/json",
                        "Authorization": "Bearer ed9e5fd5-dd4a-4dba-80d0-3f861523a561"}
        self.params = None
        self.path = "/goods/querySku"
        self.data = {"skuNo": "${skuNo}", "onCache": 0}

    def excute(self):
        self.response = self.run(1)
        self.logger.info(self.path + "done" + "\t渠道上架执行完成")
        return self.response

if __name__ == '__main__':
    spuSave().excute()


