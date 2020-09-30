import requests
#获取标列表-已有标，获取正常
url="http://192.168.150.222:8081/futureloan/mvc/api/loan/getLoanList"
r=requests.get(url)
print(r.text)




