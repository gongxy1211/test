import pytest
from api.wuhe_back import WuheBack


class Test_AppDistributeGetrecentdistributoraccount:
    data=[
        ()
    ]

    @pytest.mark.parametrize("", data)
    def test_app_distribute_getRecentDistributorAccount(self, openId, accountType):
        user = Front()
        res = user.app_distribute_getRecentDistributorAccount()
        res_json = res.json
        assert res.status_code == 200, "接口级别校验_【 获取最新的分销商支付账户接口】 " + "请求链接为：" + res.request.url
        assert res.elapsed.seconds <= 3, "接口响应超时"
        assert res_json['code'] == 0, "code校验_【 获取最新的分销商支付账户接口】 " + "请求链接为：" + res.request.url
