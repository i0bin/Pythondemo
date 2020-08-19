import requests
from time import sleep,strftime, localtime


url = "http://zt.asbk.red/app/index.php?i=2&c=entry&do=getticket&m=yunc_ticket&id=37"
headers = {
    'User-Agent':'Mozilla/5.0 (Linux; Android 10; COL-AL10 Build/HUAWEICOL-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 XWEB/2577 MMWEBSDK/200701 Mobile Safari/537.36 MMWEBID/1721 MicroMessenger/7.0.17.1720(0x270011AF) Process/toolsmp WeChat/arm64 NetType/WIFI Language/zh_CN ABI/arm64 X-Requested-With: com.tencent.mm',
    'Cookie': 'PHPSESSID=35adeb83f2c84e13355dafb87c8f40de; PHPSESSID=35adeb83f2c84e13355dafb87c8f40de',
    'Referer': 'http://zt.asbk.red/app/index.php?i=2&c=entry&do=index&m=yunc_ticket&from=singlemessage&wxref=mp.weixin.qq.com'
}
print("start: ",strftime("%Y-%m-%d %H:%M:%S", localtime()))
while True:
    result = requests.request("GET", url, headers=headers).text.encode('utf8').decode('unicode_escape')
    if '001' in result:
        print(result)
        sleep(600)
        print("wait: ",strftime("%Y-%m-%d %H:%M:%S", localtime()))
        continue
    if '<!DOCTYPE html>' in result:
        print(result[:16])
        print("stop: ",strftime("%Y-%m-%d %H:%M:%S", localtime()))
        break