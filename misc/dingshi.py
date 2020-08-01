import threading
import os
import time
url = "curl -H 'Content-Type:text/plain' --data-binary @urls.txt \"http://data.zz.baidu.com/urls?site=https://blog.l-jun.cn&token=o7OoaXucwIhOuOTL\""
def hello():
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    os.system(url)
    print("\n")
    t = threading.Timer(60, hello)
    t.start() 
print("Hi")
hello()