import re
txt = open('9yzj','r',encoding='utf-8').read()
dic = {'零':'0','一':'1','二':'2','三':'3','四':'4','五':'5','六':'6','七':'7','八':'8','九':'9'}
for w in dic:
    txt = re.sub(w,dic[w],txt)
std = re.sub(r'\D',"",txt)  
print(std)
st=re.findall(r'.{2}',std)
flag=""
for x in st:
    flag = flag + chr(int(x))
print(flag) 