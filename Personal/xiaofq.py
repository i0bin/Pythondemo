import requests
import threading
from time import sleep

#url = "http://zt.asbk.red/app/index.php?i=2&c=entry&do=getticket&m=yunc_ticket&id=" # 抢优惠券接口
url = "http://test.i0bin.cn/np.php?id=" # 本地搭建的测试接口
# PHPSESSID
# 此id对每个用户唯一，但使用时必须先要在微信公众号打开优惠券页面激活phpsessid
PHPSESSID = {
    'li' : "1c1996a6efa24864f145f76c59eb58fc",
    'hu' : "0d2eee4012322e66571b1d520e03a3b5",
    'ba' : "bb59074a026d4668b79d00828b254e4d",
    'ma' : "ce9cfd6c921df945f044dbfdf3307bf6"
}
# 收集的4个手机微信端User-Agent
ua = {
    'liua' : 'Mozilla/5.0 (Linux; Android 10; COL-AL10 Build/HUAWEICOL-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 XWEB/2577 MMWEBSDK/200701 Mobile Safari/537.36 MMWEBID/1721 MicroMessenger/7.0.17.1720(0x270011AF) Process/toolsmp WeChat/arm64 NetType/WIFI Language/zh_CN ABI/arm64 X-Requested-With: com.tencent.mm',
    'maua' : 'Mozilla/5.0 (Linux; Android 9; Redmi 8A Build/PKQ1.190319.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045318 Mobile Safari/537.36 MMWEBID/7280 MicroMessenger/7.0.14.1660(0x27000E36) Process/tools NetType/WIFI Language/zh_CN ABI/arm32 WeChat/arm32',
    'baua' : 'Mozilla/5.0 (Linux; Android 5.1; M571C Build/LMY47D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 XWEB/2577 MMWEBSDK/200502 Mobile Safari/537.36 MMWEBID/117 MicroMessenger/7.0.15.1680(0x27000F51) Process/toolsmp WeChat/arm64 NetType/WIFI Language/zh_CN ABI/arm64',
    'huua' : 'Mozilla/5.0 (Linux; Android 9; vivo X21A Build/PKQ1.180819.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045323 Mobile Safari/537.36 MMWEBID/4050 MicroMessenger/7.0.16.1700(0x2700103F) Process/tools WeChat/arm64 NetType/WIFI Language/zh_CN ABI/arm64'
}

# 请求函数
def req(name, money, PHPSESSID,uurl,ua):
    if money == 100:
        id = 36
    elif money == 50:
        id = 37
    else:
        id = 38
    headers = {
        'User-Agent': ua,
        'Cookie': 'PHPSESSID='+PHPSESSID+'; PHPSESSID='+PHPSESSID+'',
        'Referer': 'http://zt.asbk.red/app/index.php?i=2&c=entry&do=index&m=yunc_ticket&from=singlemessage&wxref=mp.weixin.qq.com'
    }
    url = uurl+str(id)
    
    while True:
        try:
            result = requests.request("GET", url, headers=headers).text.encode('utf8')
            print(name+':'+str(money)+'_'+result.decode('unicode_escape'))
            sleep(0.5) # 0.5秒发一个包，可以适当改快
        except:
            print("Error!!! ")
            #print(name+':'+str(money)+'_request timeout 3s')
            sleep(0.2) # 错误等待时间
        finally:
            pass


def threads_join(threads):
    '''
    令主线程阻塞，等待子线程执行完才继续，使用这个方法比使用join的好处是，可以ctrl+c kill掉进程
    '''
    for t in threads:
        while 1:
            if t.is_alive():
                sleep(10)
            else:
                break

# 添加线程
threads = []
for money in [100]: #[100,50,30]
    t1 = threading.Thread(target=req,args=("ba",money,PHPSESSID['ba'],url,ua['baua']))
    threads.append(t1)
for money in [50,30]:
    t1 = threading.Thread(target=req,args=("ma",money,PHPSESSID['ma'],url,ua['maua']))
    threads.append(t1)
for money in [100,50,30]:
    t1 = threading.Thread(target=req,args=("hu",money,PHPSESSID['hu'],url,ua['huua']))
    threads.append(t1)

if __name__ == "__main__": 
    print('main start')
    for t in threads:
        t.setDaemon(True)
        t.start()

    threads_join(threads)
    
    print('end main')
    

