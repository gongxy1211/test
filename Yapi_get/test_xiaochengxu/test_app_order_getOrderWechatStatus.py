import pytest
from api.wuhe_back import WuheBack


class Test_AppOrderGetorderwechatstatus:
    data=[
        ()
    ]

    @pytest.mark.parametrize("", data)
    def test_app_order_getOrderWechatStatus(self):
        user = Front()
        res = user.app_order_getOrderWechatStatus()
        res_json = res.json
        assert res.status_code == 200, "接口级别校验_【微信小程序订单状态】 " + "请求链接为：" + res.request.url
        assert res.elapsed.seconds <= 3, "接口响应超时"
        assert res_json['code'] == 0, "code校验_【微信小程序订单状态】 " + "请求链接为：" + res.request.url
