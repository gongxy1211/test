import pytest
from api.wuhe_back import WuheBack


class Test_AppDistributorFlowdetail:
    data=[
        ()
    ]

    @pytest.mark.parametrize("", data)
    def test_app_distributor_flowDetail(self, sysnumber, openId):
        user = Front()
        res = user.app_distributor_flowDetail()
        res_json = res.json
        assert res.status_code == 200, "接口级别校验_【收支明细详情】 " + "请求链接为：" + res.request.url
        assert res.elapsed.seconds <= 3, "接口响应超时"
        assert res_json['code'] == 0, "code校验_【收支明细详情】 " + "请求链接为：" + res.request.url
