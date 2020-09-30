'''
1、测试前置和后置：所有公共测试用例
2、模块级别跟函数级别的配合使用
'''
def setup_module():
    print("测试前置.整个模块开始执行")

def teardown_module():
    print("测试后置.整个模块结束后执行")

def setup_function():#也可以使用setup
    print("测试前置.每个方法开始前执行")

def teardown_function(): #也可以使用teardown
    print("测试后置.每个方法结束后执行")

def test_case01():
    print("测试用例1")
def test_case02():
    print("测试用例2")
