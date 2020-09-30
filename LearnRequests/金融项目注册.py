import  requests
#注册-手机号为空，注册异常
url="http://192.168.150.222:8081/futureloan/mvc/api/member/register"
canshu={"mobilephone":"","pwd":"123456"}
r=requests.get(url,params=canshu)
print(r.json())
# #注册-密码为空，注册异常
# url="http://192.168.150.222:8081/futureloan/mvc/api/member/register"
# canshu={"mobilephone":"13227011051","pwd":""}
# r=requests.get(url,params=canshu)
# print(r.json())
# #注册-手机号和密码为空，注册异常
# url="http://192.168.150.222:8081/futureloan/mvc/api/member/register"
# canshu={"mobilephone":"","pwd":""}
# r=requests.get(url,params=canshu)
# print(r.json())
# #注册-密码长度小于6，注册异常
# url="http://192.168.150.222:8081/futureloan/mvc/api/member/register"
# canshu={"mobilephone":"13227011051","pwd":"12345"}
# r=requests.get(url,params=canshu)
# print(r.json())
# #注册-密码长度大于18，注册异常
# url="http://192.168.150.222:8081/futureloan/mvc/api/member/register"
# canshu={"mobilephone":"13227011051","pwd":"1234567890111213141516"}
# r=requests.get(url,params=canshu)
# print(r.json())
# #注册-手机号小于11位，注册异常
# url="http://192.168.150.222:8081/futureloan/mvc/api/member/register"
# canshu={"mobilephone":"132270110","pwd":"123456"}
# r=requests.get(url,params=canshu)
# print(r.json())
# #注册-手机号大于11位，注册异常
# url="http://192.168.150.222:8081/futureloan/mvc/api/member/register"
# canshu={"mobilephone":"13227011051111","pwd":"123456"}
# r=requests.get(url,params=canshu)
# print(r.json())
# #注册-手机号含特殊字符，注册异常
# url="http://192.168.150.222:8081/futureloan/mvc/api/member/register"
# canshu={"mobilephone":"_&*227011","pwd":"123456"}
# r=requests.get(url,params=canshu)
# print(r.json())
# #注册-手机号已被注册，注册异常
# url="http://192.168.150.222:8081/futureloan/mvc/api/member/register"
# canshu={"mobilephone":"13227011051","pwd":"123456"}
# r=requests.get(url,params=canshu)
# print(r.json())
# #注册-合理的手机号、用户名、6位密码，注册成功
# url="http://192.168.150.222:8081/futureloan/mvc/api/member/register"
# canshu={"mobilephone":"13227011051","pwd":"123456","regname":"Amy"}
# r=requests.get(url,params=canshu)
# print(r.json())
# #注册-合理的手机号、用户名、8位密码，注册成功
# url="http://192.168.150.222:8081/futureloan/mvc/api/member/register"
# canshu={"mobilephone":"13227011051","pwd":"12345678","regname":"Amy"}
# r=requests.get(url,params=canshu)
# print(r.json())
# #注册-合理的手机号、用户名、18位密码，注册成功
# url="http://192.168.150.222:8081/futureloan/mvc/api/member/register"
# canshu={"mobilephone":"13227011051","pwd":"123456789101213141","regname":"Amy"}
# r=requests.get(url,params=canshu)
# print(r.json())







