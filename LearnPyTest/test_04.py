#完整的测试用例
'''
mark标记实现参数化
'''
import pytest
import requests

url="http://192.168.150.52:8089/futureloan/mvc/api/member/register"
case_data=[(18391697618,123456,"投资人","手机号码已被注册","20110",0),
           (18048,8888,"借款人","密码长度必须为6~18","20108",0)]

@pytest.mark.parametrize("mobile,pwd,rename,msg,code,status",case_data)
def test_register(mobile,pwd,rename,msg,code,status):
    print(f"测试注册功能：{mobile},{pwd},{rename}")
    param={"mobilephone":mobile,"pwd":pwd,"regname":rename}
    r=requests.post(url,data=param)
    assert  r.json()["msg"]==msg
    assert  r.json()["code"]==code
    assert  r.json()["status"]==status

# withdraw_data=[("18391697618","10")]
# # @pytest.mark.skip("该接口未实现，本版本暂不执行")
# @pytest.mark.parametrize("mobile,amount",withdraw_data)
# def test_withdraw(mobile,amount):
#     url = "http://192.168.150.52:8089/futureloan/mvc/api/member/withdraw"
#     print(f"测试取款功能：{mobile}，{amount}")
#     parm={"mobilephone":mobile,"amount":amount}
#     r=requests.post(url,data=parm)
#     assert r.json()['msg']!="服务器异常"

