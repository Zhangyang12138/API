'''
登录接口的脚本
'''
import pytest


from JinRong.baw.Member import Member
from JinRong.caw.Assert import Assert
from JinRong.caw.DataRead import DataRead


@pytest.fixture(params=DataRead().read_yaml(r"data_case\denglu_failed.yaml"))
def fail_data1(request):
    return request.param

# @pytest.fixture(params=DataRead().read_yaml(r"data_case\denglu_seccess.yaml"))
# def success_data(request):
#     return request.param



def test_fail(url1,base_requests,fail_data):
    print(f"执行登录失败的用例，测试数据为：{fail_data}")
    r = Member().login(url1, base_requests, fail_data['data'])
    # print(r.text)
    Assert().equal(fail_data['expect'], r.json(), "msg,code,status")

def test_success(url1,base_requests,success_data):
    print(f"执行登录成功的用例，测试数据为：{success_data}")
    r = Member().login(url1, base_requests, success_data['data'])
    # print(r.text)
    Assert().equal(success_data['expect'], r.json(), "msg,code,status")

