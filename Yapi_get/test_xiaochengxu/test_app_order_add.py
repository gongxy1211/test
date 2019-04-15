import pytest
from api.wuhe_back import WuheBack


class Test_AppOrderAdd:
    data=[
        ()
    ]

    @pytest.mark.parametrize("", data)
    def test_app_order_add(self, openId, recvProvinceCode, recvCityCode, recvDistCode, contactAddress, contactPerson, contactWay, goods):
        user = Front()
        res = user.app_order_add()
        res_json = res.json
        assert res.status_code == 200, "接口级别校验_【推客下单】 " + "请求链接为：" + res.request.url
        assert res.elapsed.seconds <= 3, "接口响应超时"
        assert res_json['code'] == 0, "code校验_【推客下单】 " + "请求链接为：" + res.request.url
