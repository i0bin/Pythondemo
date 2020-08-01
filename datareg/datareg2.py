filename = "txt.txt"
filename2 = "re.txt"
fo = open(filename,"r",encoding="utf-8")
ff = open(filename2,"w+",encoding="utf-8")
x = 1
y=1
for line in fo.readlines():
    line = line.strip()
    if y >= 10:
        x = 2
    if line[:2] == '\n':
        continue
    elif  line[:2] == "A.":
        ff.write('\n'+line)
        pass
    elif  line[:2] == "B.":
        ff.write(line)
        pass
    elif  line[:2] == "C.":
        ff.write(line)
        pass
    elif  line[:2] == "D.":
        ff.write(line)
        pass
    elif  line[1:3] == "答案":
        ff.write('\n正确答案：'+line[4:6]+'\n')
        pass
    elif  line[x+1:x+4] == "单选题":
        ff.write('\n'+line[:x]+"."+line[x+5:])
        y=y+1
    else:
        continue
        
fo.close()
ff.close()