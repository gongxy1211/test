import pytest
from api.wuhe_back import WuheBack


class Test_AppDistributorFlowlist:
    data=[
        ()
    ]

    @pytest.mark.parametrize("", data)
    def test_app_distributor_flowList(self, openId):
        user = Front()
        res = user.app_distributor_flowList()
        res_json = res.json
        assert res.status_code == 200, "接口级别校验_【收支明细列表】 " + "请求链接为：" + res.request.url
        assert res.elapsed.seconds <= 3, "接口响应超时"
        assert res_json['code'] == 0, "code校验_【收支明细列表】 " + "请求链接为：" + res.request.url
