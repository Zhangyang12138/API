'''
发送get请求：
1、get不带参数
2、get请求带参数
'''
import  requests  #导入包
#不带参数
# url="http://www.baidu.com"
# r=requests.get(url) #发送get请求，用r接收
# print(r.text)#文本类型的
# print(r.status_code)#状态码  200
# print(r.reason)#状态原因  ok
# print(r.cookies)#响应信息的cookies
# print(r.headers)#响应的头部信息
# print(r.raw)#原始格式的信息

#金融项目注册
#带参数
#方法1：参数拼接在URL的后面  ？号后面是参数，参数之间用&拼接。参数=值
# url="http://192.168.150.52:8089/futureloan/mvc/api/member/register?mobilephone=18391697618&pwd=123456"
# r=requests.get(url)
# print(r.text)
# print(r.json())
# print(type(r.json()))  #<class 'dict'>

#方法2：使用params传参数
# url="http://192.168.150.52:8089/futureloan/mvc/api/member/register"
# canshu={"mobilephone":"18391697618","pwd":"123456"}
# r=requests.get(url,params=canshu)
# print(r.json())
#
# url="http://192.168.150.52:8089/futureloan/mvc/api/member/register?mobilephone=18391697618&pwd="
# r=requests.get(url)
# print(r.text)

#httpbin ,一个测试网站，有get/post等接口，参数任意构造，服务器将发送的请求转成json格式的返回
# r=requests.get("http://www.httpbin.org/get?username=123&pwd=456&email=123456@qq.com")
# print(r.text)
#练习
# url="https://tcc.taobao.com/cc/json/mobile_tel_segment.htm?tel=18391697618"
# r=requests.get(url)
# print(r.text)

#发送的请求带请求头
#设置User-Agent,伪装成浏览器发送的请求
headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"}
r=requests.get("http://www.httpbin.org/get?username=123&pwd=456&email=123456@qq.com",headers=headers)
print(r.text)



