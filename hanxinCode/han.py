from PIL import Image 
# list = ['G','B','R']
# img_R = Image.open("R.png",'r')
# img_G = Image.open("G.png",'r')
# img_B = Image.open("B.png",'r')
# print("R宽"+ str(img_R.size[0]),"高"+str(img_R.size[1]))
# print("G宽"+ str(img_G.size[0]),"高"+str(img_G.size[1]))
# print("B宽"+ str(img_B.size[0]),"高"+str(img_B.size[1]))
# img_R = img_R.convert('RGBA')
# str_strlist = img_R.load()
# data = str_strlist[1,1]
# for x in list:R
#     print(x)R
o_img = "miscR.png"
o = "R"
img = Image.open(o_img,'r')
width = img.size[0]
heigth = img.size[1]
# img2 = img.crop((0,h1,width,heigth/10))
# print(img2)
# img2.save("save.png",'png')
h1 = 2
h0 = heigth/12
h2 = heigth/12+2
i = 1
print("B宽"+ str(width),"高"+str(heigth))
while(h1<heigth):
    file = o+str(i)+".png"
    # img2 = img.crop((0,h1,width,h2))
    # img2.save(file,'png')
    print(file,h1,h2)
    h1 = h2
    h2 +=h0
    i+=1

    

