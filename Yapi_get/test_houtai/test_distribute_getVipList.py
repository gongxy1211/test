import pytest
from api.wuhe_back import WuheBack


class Test_DistributeGetviplist:
    data=[
        ()
    ]

    @pytest.mark.parametrize("", data)
    def test_distribute_getVipList(self, pageNum, pageSize, name, startTime, endTime, distributerId, dieticianSysnumber, packageStatus, belongedSalesId):
        user = Front()
        res = user.distribute_getVipList()
        res_json = res.json
        assert res.status_code == 200, "接口级别校验_【获取会员列表】 " + "请求链接为：" + res.request.url
        assert res.elapsed.seconds <= 3, "接口响应超时"
        assert res_json['code'] == 0, "code校验_【获取会员列表】 " + "请求链接为：" + res.request.url
