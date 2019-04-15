import pytest
from api.wuhe_back import WuheBack


class Test_MembersStagestatus:
    data=[
        ()
    ]

    @pytest.mark.parametrize("", data)
    def test_members_stageStatus(self):
        user = Front()
        res = user.members_stageStatus()
        res_json = res.json
        assert res.status_code == 200, "接口级别校验_【获取疗程状态】 " + "请求链接为：" + res.request.url
        assert res.elapsed.seconds <= 3, "接口响应超时"
        assert res_json['code'] == 0, "code校验_【获取疗程状态】 " + "请求链接为：" + res.request.url
