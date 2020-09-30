import requests
#登录-手机号为空，登录异常
url="http://192.168.150.222:8081/futureloan/mvc/api/member/login"
canshu={"mobilephone":"","pwd":"123456"}
r=requests.get(url,params=canshu)
print(r.json())
#登录-密码为空，登录异常
# url="http://192.168.150.222:8081/futureloan/mvc/api/member/login"
# canshu={"mobilephone":"13227011051","pwd":""}
# r=requests.get(url,params=canshu)
# print(r.json())
# #登录-手机号、密码都为空，登录异常
# url="http://192.168.150.222:8081/futureloan/mvc/api/member/login"
# canshu={"mobilephone":"","pwd":""}
# r=requests.get(url,params=canshu)
# print(r.json())
# #登录-手机号错误，登录异常
# url="http://192.168.150.222:8081/futureloan/mvc/api/member/login"
# canshu={"mobilephone":"13227011000","pwd":"123456"}
# r=requests.get(url,params=canshu)
# print(r.json())
# #登录-密码错误，登录异常
# url="http://192.168.150.222:8081/futureloan/mvc/api/member/login"
# canshu={"mobilephone":"13227011051","pwd":"111111"}
# r=requests.get(url,params=canshu)
# print(r.json())
# #登录-手机号、密码错误，登录异常
# url="http://192.168.150.222:8081/futureloan/mvc/api/member/login"
# canshu={"mobilephone":"13227011000","pwd":"111111"}
# r=requests.get(url,params=canshu)
# print(r.json())
# #登录-手机号未注册，登录异常
# url="http://192.168.150.222:8081/futureloan/mvc/api/member/login"
# canshu={"mobilephone":"15200622363","pwd":"111111"}
# r=requests.get(url,params=canshu)
# print(r.json())
# #登录-手机号、密码正确，登录正常
# url="http://192.168.150.222:8081/futureloan/mvc/api/member/login"
# canshu={"mobilephone":"13227011051","pwd":"123456"}
# r=requests.get(url,params=canshu)
# print(r.json())







