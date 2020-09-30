'''
fixture带参数
'''
import pytest
import requests

data=[{"data":{"mobilephone":"18391697618","pwd":"123456"},"expect":{"msg":"手机号码已被注册","code":"20110","status":0}},
      {"data":{"mobilephone":"18398728198","pwd":"1234"},"expect":{"msg":"密码长度必须为6~18","code":"20108","status":0}}]
@pytest.fixture(params=data)
def register_data(request):#request是fixture中的关键字
    return  request.param#通过request.param获取每一组测试数据

def test_register(register_data):
    print(register_data)
    r=requests.post("http://192.168.150.52:8089/futureloan/mvc/api/member/register",register_data['data'])
    assert  r.json()['msg']==register_data['expect']['msg']
    assert r.json()['code'] == register_data['expect']['code']
    assert r.json()['status'] == register_data['expect']['status']

def test_list():
    r = requests.post("http://192.168.150.52:8089/futureloan/mvc/api/member/list")
    print(r.text)

