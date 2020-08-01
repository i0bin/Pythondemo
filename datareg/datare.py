filename = "txt.txt"
filename2 = "re.txt"
fo = open(filename,"r",encoding="utf-8")
ff = open(filename2,"w+",encoding="utf-8")
x = 1
for line in fo.readlines():
    line = line.strip()
    
    if line[:2] == '\n':
        pass
    elif  line[:2] == "A.":
        ff.write('\n'+line)
        pass
    elif  line[:2] == "正确":
        ff.write('\n'+line[:7]+'\n')
        pass
    elif  line[:2] == "展开":
        pass
    elif  line[:2] == "2分":
        ff.write('\n'+str(x)+".")
        x+=1
        pass
    else:
        ff.write(line)
        
fo.close()
ff.close()