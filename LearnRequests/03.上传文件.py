'''
上传文件
'''
import  requests
#上传一个文件
# url="http://www.httpbin.org/post"
# file_path="d:/1.png"
# with open(file_path,mode='rb') as f:
    # 二元祖:'name':file-tuple('filename',fileobj)
    # file={"1.png":(file_path,f)}
    # r=requests.post(url,files=file)
    # print(r.text)

    #三元组：’name':file-tuple,file-tuple为（'filename',fileobj,'content-type,'）
    #content_type  指的是MIME类型
    # file={"1.png":(file_path,f,"image/png")}
    # r=requests.post(url,files=file)
    # print(r.text)

#上传多个文件
url="http://www.httpbin.org/post"
file_path1="d:/1.png"
file_path2="d:/1.txt"
# with open(file_path1,mode='rb')as  f1:
#     with open(file_path2,mode='r',encoding='UTF-8')as f2:
#         files={"1.png":(file_path1,f1,"image/png"),
#                "1.txt":(file_path2,f2,"text/plain")}
#         r=requests.post(url,files=files)
#         print(r.text)

# 使用data上传文件，一次只能上传一个文件
with open(file_path2,mode='rb')as  f2:
    #print(f2.read())
    r=requests.post(url,data=f2)
    print(r.text)

