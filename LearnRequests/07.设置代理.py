'''
1、爬虫之类的场景，避免服务器认为是攻击，将IP屏蔽掉
2、代理抓包，定位问题
'''
import requests

proxy={
    "http":"http://127.0.0.1:8888",
    "https":"http://127.0.0.1:8888"
}
r=requests.get("http://www.httpbin.org",proxies=proxy)
print(r.status_code)
print(r.text)



























