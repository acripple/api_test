import requests 

res = requests.get("https://www.baidu.com") 
print(res.status_code, res.reason) # 200 OK
print(res.text) # 文本格式，有乱码
print(res.content) # 二进制格式
print(res.encoding) # 查看解码格式 ISO-8859-1
print(res.apparent_encoding) # utf-8
res.encoding='utf-8' # 手动设置解码格式为utf-8
print(res.text) # 乱码问题被解决
print(res.cookies.items()) # cookies中的所有的项 [('BDORZ', '27315')]
print(res.cookies.get("BDORZ")) # 获取cookies中BDORZ所对应的值 27315