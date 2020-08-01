from PIL import Image
img = Image.open("d:\\Documents\\python\\hanxin\\misc2.png")
r,g,b=img.split()
r.save("d:\\Documents\\python\\hanxin\\miscR.png")
g.save("d:\\Documents\\python\\hanxin\\miscG.png")
b.save("d:\\Documents\\python\\hanxin\\miscB.png")