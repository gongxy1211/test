import pytest
from api.wuhe_back import WuheBack


class Test_AppOrderGetlist:
    data=[
        ()
    ]

    @pytest.mark.parametrize("", data)
    def test_app_order_getList(self, openId, orderStatus, pageNum, pageSize):
        user = Front()
        res = user.app_order_getList()
        res_json = res.json
        assert res.status_code == 200, "接口级别校验_【我的订单列表】 " + "请求链接为：" + res.request.url
        assert res.elapsed.seconds <= 3, "接口响应超时"
        assert res_json['code'] == 0, "code校验_【我的订单列表】 " + "请求链接为：" + res.request.url
