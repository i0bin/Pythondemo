#!usr/bin/python
# -*- coding: utf-8 -*-
import requests
import urllib

url_1 = "http://10.0.0.12/Cardholder/ShowImage.aspx?AccNum=180204" #180204'831' 后三位for 100 -- 999
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
cookie="ASP.NET_SessionId=ig4mfv1v14e1bhtund3ddbqk"
cookie_dict = {i.split("=")[0]:i.split("=")[-1] for i in cookie.split("; ")}

for x in range(100,102):
    url = " "
    url = url_1 + str(x)
    response = requests.get(url, headers = headers, cookies = cookie_dict)	
    name = str(x) + ".jpg" #保存格式 数字.jpg
    with open(name, 'wb+') as f:  
        f.write(response.content)
