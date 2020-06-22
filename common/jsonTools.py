import json

class jsonTools:
    
    #传入json字典
    def modifyJson(self,jsonDict,k,v):
        for key in jsonDict.keys():
            if k == key:
                jsonDict[k] = v
        return json.dumps(jsonDict)
    
    #取单个值
    def getValue(self,jsonDict,k):
        for key in jsonDict.keys():
            print(key)
            if k == key:
                return jsonDict[k]
        return None
    
    #批量取值，支持遍历四层
    def getJsonValue(self, jsonDict, keyList):
        valueList = []
        for key in keyList:
            if key.__len__() == 1:
                valueList.append(jsonDict[key[0]])
            if key.__len__() == 2:
                valueList.append(jsonDict[key[0]][key[1]])
            if key.__len__() == 3:
                valueList.append(jsonDict[key[0]][key[1]][key[2]])
            if key.__len__() == 4:
                valueList.append(jsonDict[key[0]][key[1]][key[2]][key[3]])
        return valueList

if __name__ == '__main__':
    print(jsonTools().modifyJson({"asd":1,"ww":2},"ww","asdad"))