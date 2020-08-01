import requests
i=0
for x in range(0,10): #秒数个位
    for y in range(0,10): #秒数十位
        for m_g in range(1,7): #分钟个位
            for m_s in range(0,2): #分钟十位
                file = str(i)+".jpg"
                url = "http://www.efittech.com/upload/pics/pic_2020051014"+str(m_s)+str(m_g)+str(y)+str(x)+".png"
                with open(file,"wb") as f:
                    f.write(requests.get(url).content)
                i+=1
print(i) #图片数
