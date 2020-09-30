'''
1、测试前置和后置
2、类级别和方法级别
'''

#测试类使用Test开头，里面不能有_init_构造方法
class TesClass:
    # def __init__(self):
    def setup_class(self):
        print("测试前置.类里面所有用例开始前执行")

    def teardowm_class(self):
        print("测试后置.类里面所有用例结束后执行")

    def setup(self):
        print("测试前置.每个方法前执行")

    def teardown(self):
        print("测试后置.每个方法后执行")

    def test_case01(self):
        print("用例1")

    def test_case02(self):
        print("用例2")
