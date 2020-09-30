'''
脚本层的公共方法
'''

import pytest

#读取环境文件，获取url
from JinRong.baw.DbOp import DbOp
from JinRong.baw.Member import Member
from JinRong.caw.Assert import Assert

from JinRong.caw.BaseRequests import BaseRequests
from JinRong.caw.DataRead import DataRead

ENVPATH=r'data_env\env.ini'
@pytest.fixture(scope='session')
def url():
    return DataRead().read_ini(ENVPATH,'url')

#
@pytest.fixture(scope='session')
def db():
    return eval(DataRead().read_ini(ENVPATH,'db'))

@pytest.fixture(scope='session')
def base_requests():
    return BaseRequests()

@pytest.fixture(scope="session", params=DataRead().read_yaml(r"data_case\denglu_seccess.yaml"))
def success_data(request):
    return request.param

@pytest.fixture(scope='session')
def register(url,base_requests,success_data,db):
    #注册用户
    r=Member().register(url,base_requests,success_data['data'])
    Assert().equal(success_data['expect'],r.json(),"msg,code,status")
    yield
    #删除注册用户
    DbOp().delete_user(db,success_data['data']['mobilephone'])


