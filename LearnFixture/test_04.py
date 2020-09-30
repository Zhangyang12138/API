'''
fixture带返回值
'''
import pytest
@pytest.fixture
def data():
    return {"username":"root","pwd":"123456"}

def test_case01(data):#函数可以做参数使用，也可做返回值使用
    print(f"{data}")
    print(f"{data['username']}")
    print(f"{data['pwd']}")



