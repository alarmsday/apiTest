import common.configHttp as http
from common.Log import MyLog as Log
import json
import common.jsonTools as jsonTools

class SpuQuery:
    def __init__(self):
        self.log = Log.get_log()
        self.jsonTool = jsonTools()
        self.logger = self.log.logger
        self.headers  = {"Content-Type": "application/json", "Authorization": "Bearer ed9e5fd5-dd4a-4dba-80d0-3f861523a561"}
        self.host = "http://java.goodscenter.mng.turboradio.cn"
        self.data = {"pageNum":1,"pageSize":10}

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