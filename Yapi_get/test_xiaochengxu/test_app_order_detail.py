import pytest
from api.wuhe_back import WuheBack


class Test_AppOrderDetail:
    data=[
        ()
    ]

    @pytest.mark.parametrize("", data)
    def test_app_order_detail(self, sysnumber):
        user = Front()
        res = user.app_order_detail()
        res_json = res.json
        assert res.status_code == 200, "接口级别校验_【订单详情】 " + "请求链接为：" + res.request.url
        assert res.elapsed.seconds <= 3, "接口响应超时"
        assert res_json['code'] == 0, "code校验_【订单详情】 " + "请求链接为：" + res.request.url
