'''
自动管理Cookie
'''
import  requests

#新建一个session，通过session自动管理cookie
s=requests.session()
#访问首页前，打印session自动管理cookie
# print(s.cookies)
# print(requests.utils.dict_from_cookiejar(s.cookies))

#访问百格的首页
r=s.get("https://www.bagevent.com")
#访问首页之后，打印cookie，cookie有两条
# print(s.cookies)
# print(requests.utils.dict_from_cookiejar(s.cookies))

param={
    "access_type":1,
    "loginType":1,
    "emailLoginWay":0,
    "account":"2780487875@qq.com",
    "password":"qq2780487875",
    "remindmeBox":"on",
    "remindme":1
}
r=s.post("https://www.bagevent.com/user/login",data=param)
# print("登录之后，打印cookie，cookie有5条")
# print(s.cookies)
# print(requests.utils.dict_from_cookiejar(s.cookies)) #CookieJar转字典

r=s.get("http://www.bagevent.com/vlist/common/surveyList")
print(r.json())
print(r.json()["list"][0]["survey_id"])