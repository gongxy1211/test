import pytest
from api.wuhe_back import WuheBack


class Test_DistributeGetalldistributerlist:
    data=[
        ()
    ]

    @pytest.mark.parametrize("", data)
    def test_distribute_getAllDistributerList(self):
        user = Front()
        res = user.distribute_getAllDistributerList()
        res_json = res.json
        assert res.status_code == 200, "接口级别校验_【获取上级推客列表（会员管理）】 " + "请求链接为：" + res.request.url
        assert res.elapsed.seconds <= 3, "接口响应超时"
        assert res_json['code'] == 0, "code校验_【获取上级推客列表（会员管理）】 " + "请求链接为：" + res.request.url
