'''
fixture:灵活的前置/后置
'''
import  pytest

@pytest.fixture(autouse=True) #测试用例会自动使用，不需要作为参数传递
def data():
    print("准备测试数据")

@pytest.fixture() #测试前置，需要执行该前置的地方，将函数名作为参数传入即可
def login():
    print("登录功能") #yield之前，测试前置
    yield
    print("退出登录") #yield之后，测试后置
    print("用例执行完毕")

def test_register(): #login作为参数传进来
    print("注册功能，不用登录")

def test_recharge(login):
    print("充值功能，需要先登录")

@pytest.mark.usefixtures("login")#也可以使用userfixtures
def test_withdraw():
    print("取现功能，需要登录")