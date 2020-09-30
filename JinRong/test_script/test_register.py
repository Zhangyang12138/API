'''
注册接口的脚本
'''

#pytest fixture 参数化的功能
#参数读进来
import pytest

from JinRong.baw.DbOp import DbOp
from JinRong.baw.Member import Member
from JinRong.caw.Assert import Assert

from JinRong.caw.DataRead import DataRead



@pytest.fixture(params=DataRead().read_yaml(r"data_case\register_fail.yaml"))
def fail_data(request):
    return request.param

@pytest.fixture(params=DataRead().read_yaml(r"data_case\zhuce_seccess.yaml"))
def success_data(request):
    return request.param

@pytest.fixture(params=DataRead().read_yaml(r"data_case\register_repeat.yaml"))
def repeat_data1(request):
    return  request.param

# @pytest.fixture()
# def register(url1,base_requests,success_data,db1):
#     #注册用户
#     r=Member().register(url1,base_requests,success_data['data'])
#     yield
#     #删除注册用户
#     DbOp().delete_user(db,success_data['data']['mobilephone'])



# 注册失败的逻辑
def test_register_fail(fail_data,url1,base_requests):
    print(f"执行注册失败的用例，测试数据为：{fail_data}")
    #conftest.py
    r=Member().register(url1,base_requests,fail_data['data'])
    # print(r.text)
    # assert str(fail_data['expect']['msg'])==str(r.json()['msg'])
    # assert str(fail_data['expect']['code']) == str(r.json()['code'])
    # assert str(fail_data['expect']['status']) == str(r.json()['status'])
    Assert().equal(fail_data['expect'],r.json(),"msg,code,status")

#注册成功的逻辑
def test_register_success(success_data,url1,base_requests,db1):
    print(f"执行注册成功的用例，测试数据为：{success_data}")
    r=Member().register(url1,base_requests,success_data['data'])
    # print(r.text)
    Assert().equal(success_data['expect'], r.json(), "msg,code,status")
    #清理环境
    DbOp().delete_user(db1,success_data['data']['mobilephone'])
    # assert str(success_data['except']['msg'])== str(r.json()['msg'])
    # assert str(success_data['except']['code']) == str(r.json()['code'])
    # assert str(success_data['except']['status']) == str(r.json()['status'])

# #重复注册的逻辑
def test_repeat(repeat_data1,url1,base_requests):
    print(f"执行重复注册的用例，测试数据为：{repeat_data1}")
    r = Member().register(url1, base_requests, repeat_data1['data'])
    # print(r.text)
    # assert str(repeat_data1['except']['msg']) == str(r.json()['msg'])
    # assert str(repeat_data1['except']['code']) == str(r.json()['code'])
    # assert str(repeat_data1['except']['status']) == str(r.json()['status'])
    Assert().equal(repeat_data1['expect'], r.json(), "msg,code,status")




