import pytest
from api.wuhe_back import WuheBack


class Test_AppDistributeUploadfileorigin:
    data=[
        ()
    ]

    @pytest.mark.parametrize("", data)
    def test_app_distribute_uploadFileOrigin(self, file):
        user = Front()
        res = user.app_distribute_uploadFileOrigin()
        res_json = res.json
        assert res.status_code == 200, "接口级别校验_【分销系统 图片原尺寸上传】 " + "请求链接为：" + res.request.url
        assert res.elapsed.seconds <= 3, "接口响应超时"
        assert res_json['code'] == 0, "code校验_【分销系统 图片原尺寸上传】 " + "请求链接为：" + res.request.url