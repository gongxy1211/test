import pytest
from api.wuhe_back import WuheBack


class Test_DistributeGetdistributorlevellist:
    data=[
        ()
    ]

    @pytest.mark.parametrize("", data)
    def test_distribute_getDistributorLevelList(self):
        user = Front()
        res = user.distribute_getDistributorLevelList()
        res_json = res.json
        assert res.status_code == 200, "接口级别校验_【获取推客等级列表接口】 " + "请求链接为：" + res.request.url
        assert res.elapsed.seconds <= 3, "接口响应超时"
        assert res_json['code'] == 0, "code校验_【获取推客等级列表接口】 " + "请求链接为：" + res.request.url
