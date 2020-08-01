# *_*coding:utf-8 *_* 
# Author: ynm3000 https://ctf.show
# 标准当铺密码加密解密，空格分割
#python2
#python2
print("only support python2")
code = "田由中人工大王夫井羊".decode('utf-8')
split = ' '


def encode(s):
    s=s.decode('utf-8')
    buff = ""
    if len(s) > 0:
        for c in s:
            str1 = str(ord(c))
            for st in str1:
                buff += code[int(st)]
            buff += split
    return buff


def decode(s):
    s = s.decode('utf-8')
    buff = ""
    temp = ""
    if len(s) > 0:
        stringList = s.split(split)
        for s1 in stringList:
            for s2 in s1:
                index = code.find(s2)
                if index > -1:
                    temp += str(index)
            buff += chr(int(temp))
            temp = ''
    return buff

print(decode('由田中 由田井 羊夫 由田人 由中人 羊羊 由由王 由田中 由由大 由田工 由由由 由由羊 由中大'))
