import pytest
from api.wuhe_back import WuheBack


class Test_OrderOrderstatus:
    data=[
        ()
    ]

    @pytest.mark.parametrize("", data)
    def test_order_orderStatus(self):
        user = Front()
        res = user.order_orderStatus()
        res_json = res.json
        assert res.status_code == 200, "接口级别校验_【获取订单枚举类】 " + "请求链接为：" + res.request.url
        assert res.elapsed.seconds <= 3, "接口响应超时"
        assert res_json['code'] == 0, "code校验_【获取订单枚举类】 " + "请求链接为：" + res.request.url
