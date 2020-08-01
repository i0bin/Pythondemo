#/usr/bin/env python
#coding:utf-8
import base64
def base(s):
    try:
        s = base64.b32decode(s)
        s = base(s)
    except:
        try:
            s = base64.b64decode(s)
            s = base(s)
        except:
            return s
    return s
f = open('base\\1.txt')

text = f.read()

print(base(text))
