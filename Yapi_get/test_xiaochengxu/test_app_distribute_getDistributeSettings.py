import pytest
from api.wuhe_back import WuheBack


class Test_AppDistributeGetdistributesettings:
    data=[
        ()
    ]

    @pytest.mark.parametrize("", data)
    def test_app_distribute_getDistributeSettings(self):
        user = Front()
        res = user.app_distribute_getDistributeSettings()
        res_json = res.json
        assert res.status_code == 200, "接口级别校验_【获取分销设置信息接口 (基础设置,特权说明，提现设置)】 " + "请求链接为：" + res.request.url
        assert res.elapsed.seconds <= 3, "接口响应超时"
        assert res_json['code'] == 0, "code校验_【获取分销设置信息接口 (基础设置,特权说明，提现设置)】 " + "请求链接为：" + res.request.url
