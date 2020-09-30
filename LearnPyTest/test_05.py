'''
自定义标记
'''
import pytest
@pytest.mark.smoke #冒烟测试用例
def test_case01():
    print("test_case01")

@pytest.mark.func #func 功能测试用例
def test_case02():
    print("test_case02")

@pytest.mark.func #在类上面修饰时，对类里面的方法全部都生效
class TestClass:
    def test_case03(self): #带有func标签
        print("test_case03")
    def test_case04(self):#带有func标签
        print("test_case04")
    def test_case05(self):#带有func标签
        print("test_case05")


