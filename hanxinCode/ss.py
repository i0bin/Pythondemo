from PIL import Image
import os

# 图片地址 https://f.i0bin.cn/misc2.png
resultfile = 'result.png' #最终输图片名
list = ['G','B','R']
def GetRGB(): # 分离R,G,B通道
    img = Image.open("misc2.png")
    r,g,b=img.split()
    r.save("miscR.png")
    g.save("miscG.png")
    b.save("miscB.png")

def Gethan(): # 分别得R,G,B的到每一行
    for rgb in list:
        o_img = "misc"+rgb+".png"
        img = Image.open(o_img,'r')
        width = img.size[0]
        heigth = img.size[1] 
        h0 = 1   
        if rgb == 'G':
            h1 = 1
            h2 = 2
        elif rgb == 'B':
            h1 = 1
            h2 = 2
            heigth = heigth - 1
        elif rgb == 'R':
            h1 = 2
            h2 = 3
        i = 1
        while(h1<heigth):
            file = rgb+str(i)+".png"
            img2 = img.crop((0,h1,width,h2))
            img2.save(file,'png')
            h1 = h2
            h2 += h0
            i+=1
        os.remove(o_img)

def GetNewImg():
    imagefile = []
    for i in range(1,12):
        for x in list: # 按照G,B,R顺序读取
            if (i==11 and x == 'B') or (i==11 and x == 'R'):
                break
            filename = x+str(i)+".png"
            fileopen = Image.open(filename)
            imagefile.append(fileopen) # 将图片内容添加到数组中
    target = Image.new("RGB",(36,31))# 新建一个36*31的空白图片
    left = 0
    right = 1
    slze = (0,left,36,right)
    for i in range(0,31):
        target.paste(imagefile[i],slze)
        target.save('Temp.png',quality=100)
        if i != 30:
            slze = (0,left+imagefile[i].size[1],36,right+imagefile[i+1].size[1])
            left+=imagefile[i].size[1]
            right+=imagefile[i+1].size[1]
    
def RmTmpImg():# 删除过程中的临时文件
    for i in range(1,12):
        for x in list:
            if (i==11 and x == 'B') or (i==11 and x == 'R'):
                break
            filename = x+str(i)+".png"
            os.remove(filename)
    os.remove('Temp.png')

def Vert(): # 变换
    img = Image.open('Temp.png')
    out = img.transpose(Image.FLIP_TOP_BOTTOM)
    N = img.crop((27,0,34,7))
    out.paste(N,(3,24,10,31))
    out.save(resultfile,'png')
    out.show()

if __name__ == "__main__":
    GetRGB()
    Gethan()
    GetNewImg()
    Vert()
    RmTmpImg()
