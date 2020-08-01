from PIL import Image

list = ['G','B','R']
imagefile = []
he = 0
path = "d:\\Documents\\python\\hanxin\\"
for i in range(1,12):
    for x in list:
        if (i==11 and x == 'B') or (i==11 and x == 'R'):
            break
        filename = path+x+str(i)+".png"
        imagefile.append(Image.open(filename))
        print(filename)
        print("宽:"+str(Image.open(filename).size[0]),"高:"+str(Image.open(filename).size[1]))
        he+=Image.open(filename).size[1]
print(he)
target = Image.new("RGB",(36,31))
print(target)
left = 0
right = 1
slze = (0,left,36,right)
for i in range(0,31):
    print(imagefile[i].size[1],imagefile[i].size[0])
    print(slze,i)
    target.paste(imagefile[i],slze)
    target.save('result.jpg',quality=100)
    if i != 30:
        slze = (0,left+imagefile[i].size[1],36,right+imagefile[i+1].size[1])
        left+=imagefile[i].size[1]
        right+=imagefile[i+1].size[1]
