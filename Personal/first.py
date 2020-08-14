import requests

url = "http://zt.aasbk.red/app/index.php?i=2&c=entry&do=getticket&m=yunc_ticket&id=37"


headers = {
  'User-Agent': 'Mozilla/5.0 (Linux; Android 10; COL-AL10 Build/HUAWEICOL-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 XWEB/2577 MMWEBSDK/200701 Mobile Safari/537.36 MMWEBID/1721 MicroMessenger/7.0.17.1720(0x270011AF) Process/toolsmp WeChat/arm64 NetType/WIFI Language/zh_CN ABI/arm64 X-Requested-With: com.tencent.mm',
  'Cookie': 'PHPSESSID=1c1996a6efa24864f145f76c59eb58fc; PHPSESSID=1c1996a6efa24864f145f76c59eb58fc',
  'Referer': 'http://zt.asbk.red/app/index.php?i=2&c=entry&do=index&m=yunc_ticket&from=singlemessage&wxref=mp.weixin.qq.com'
}

print(headers)

response = requests.request("GET", url, headers=headers, timeout=2)

print(response.text.encode('utf8'))
