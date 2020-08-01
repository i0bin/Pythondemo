from PIL import Image
img = Image.open("miscR.png")
w,h = img.size
print(img,w,h)
for x in range(0,36):
    for y in range(0,12):
        print(img.load()[x,y],end=",")

