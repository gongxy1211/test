import pytest
from api.wuhe_back import WuheBack


class Test_AppGoodsGetlist:
    data=[
        ()
    ]

    @pytest.mark.parametrize("", data)
    def test_app_goods_getList(self):
        user = Front()
        res = user.app_goods_getList()
        res_json = res.json
        assert res.status_code == 200, "接口级别校验_【产品列表接口】 " + "请求链接为：" + res.request.url
        assert res.elapsed.seconds <= 3, "接口响应超时"
        assert res_json['code'] == 0, "code校验_【产品列表接口】 " + "请求链接为：" + res.request.url
