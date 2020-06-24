import pytest,os
from datetime import datetime
import apiLib.goodsCenter.goodsCenterApi as gc
import allure

class parma:
    spuId = None
    detilsCode = None
    skuNo = None

class TestGoodsPutOn:

    def test_spuSave(self):
        spu = gc.goodsCenterApi()

