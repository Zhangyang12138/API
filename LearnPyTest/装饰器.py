'''
装饰器：运行中增加功能的一种方式
在原来的用例上增加一些新功能
'''
#已经写好了一些测试用例，后面维护代码时，想增强这些用例的功能，比如日志，又不想改test_case01、test_case02的代码
#将日志的功能定义成一个装饰器，装饰器只拿函数作为参数

def log(func):
    #*args,**kw的目的：func可以有任意个参数
    def wrapper(*args,**kw):
        #每个函数有一个__name__属性，返回函数的名字
        print(f"in 函数：{func.__name__}")
        func(*args,**kw)
        print(f"out 函数：{func.__name__}")
    return  wrapper

def test_case01():
    print("in 函数：test_case01")
    print("用例1")
    print("out 函数：test_case02")

@log
def test_case02():
    print("用例2")
@log
def test_case03():
    print("用例3")