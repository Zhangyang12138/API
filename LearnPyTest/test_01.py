'''
测试文件已test_开头
测试函数/方法以test_开头
'''
#接口
def add(a,b):
    try:
        return  a+b
    except Exception as e:
        return str(e).strip()

#为上面的函数设计测试用例，每个用例用test_开头
'''
上面接口的测试用例
'''
#整数的加法
def test_case01():
    r=add(1,2)#调用上面的结果
    assert r==3#校验结果
#列表的加法
def test_case02():
    r=add([1,2],[3,4])
    assert r==[1,2,3,4]
#浮点数的加法
def test_case03():
    r=add(0.1,0.2)
    assert r==0.3
#整数和字符串的加法
def test_case04():
    r=add(1,'2')
    assert r==""