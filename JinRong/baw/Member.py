'''
业务AW：按模块划分
business action word
'''
from JinRong.caw.BaseRequests import BaseRequests

REGISTER="/futureloan/mvc/api/member/register"
LOGIN="/futureloan/mvc/api/member/login"
class Member:
    def register(self,url1,base_requests,data):
        '''
        用户注册的接口
        :param url: 环境信息 http://host：post/
        :param base_requests:
        :param data:数据
        :return:响应信息
        '''
        real_url=url1+REGISTER
        r=base_requests.post(real_url,data=data)
        return r

    def login(self,url1,base_requests,data):
        '''

        :param url:
        :param data:
        :param base_requests:
        :return:
        '''
        real_url=url1+LOGIN
        r=base_requests.post(real_url,data=data)
        return r

if __name__=='__main__':
    r=Member().register("http://192.168.150.52:8089",BaseRequests(),{"pwd":"18391697618"})
    print(r.text)
    r = Member().login("http://192.168.150.52:8089", BaseRequests(), {"pwd": "123456"})
    print(r.text)