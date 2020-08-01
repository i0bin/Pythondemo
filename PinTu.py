import random
import pygame
import os
# 初始化
pygame.init()
# 窗口标题
pygame.display.set_caption('PinTu')
# 窗口大小
s = pygame.display.set_mode((660, 660))

# 绘图地图
imgMap = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]

# 判断胜利的地图
winMap = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]
#下载图片
IMAGE_URL = "https://l-jun.cn/11.jpg"
def request_download():
    import requests
    r = requests.get(IMAGE_URL)
    with open('./b798abe6e1b1318ee36b0dcb3fb9e4d3.jpg', 'wb') as f: #'img'的MD5值'b798abe6e1b1318ee36b0dcb3fb9e4d3'
        f.write(r.content)

def search_file(dir,img_name):#本地搜索拼图图片
    flag = 0
    for root,dirs,files in os.walk(dir):
        for file in files:
            if file == img_name:
                flag = 1
                break
            else:
                flag = 0
        if flag == 1:
            break
    if flag == 1:
        print("Search Image Success, Start Game!")
    else:
        print("Not Found Image, Start Download! ")
        request_download()

search_file('./','b798abe6e1b1318ee36b0dcb3fb9e4d3.jpg')


# 游戏的单击事件
def click(x, y, map):
    if y - 1 >= 0 and map[y - 1][x] == 8:
        map[y][x], map[y - 1][x] = map[y - 1][x], map[y][x]
    elif y + 1 <= 2 and map[y + 1][x] == 8:
        map[y][x], map[y + 1][x] = map[y + 1][x], map[y][x]
    elif x - 1 >= 0 and map[y][x - 1] == 8:
        map[y][x], map[y][x - 1] = map[y][x - 1], map[y][x]
    elif x + 1 <= 2 and map[y][x + 1] == 8:
        map[y][x], map[y][x + 1] = map[y][x + 1], map[y][x]


# 打乱地图
def randMap(map):
    for i in range(1000):
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        click(x, y, map)


# 加载图片
img = pygame.image.load('./b798abe6e1b1318ee36b0dcb3fb9e4d3.jpg')
# 随机地图
randMap(imgMap)
# 游戏主循环
while True:
    # 延时32毫秒,相当于FPS=30
    pygame.time.delay(32)
    for event in pygame.event.get():
        # 窗口的关闭事件
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:  # 鼠标单击事件
            if pygame.mouse.get_pressed() == (1, 0, 0):  # 鼠标左键按下
                mx, my = pygame.mouse.get_pos()  # 获得当前鼠标坐标
                if mx < 660 and my < 660:  # 判断鼠标是否在操作范围内
                    x = int(mx / 220)  # 计算鼠标点到了哪个图块
                    y = int(my / 220)
                    click(x, y, imgMap)  # 调用单击事件
                    if imgMap == winMap:  # 如果当前地图情况和胜利情况相同,就print胜利
                        print("You WIN!!")

    # 背景色填充
    s.fill((222, 200, 250))
    # 绘图
    for y in range(3):
        for x in range(3):
            i = imgMap[y][x]
            if i == 8:  # 8号图块不用绘制
                continue
            dx = (i % 3) * 220  # 计算绘图偏移量
            dy = (int(i / 3)) * 220
            s.blit(img, (x * 220, y * 220), (dx, dy, 220, 220))
    # 画参考图片
    #s.blit(img, (1090, 0))
    # 刷新界面
    pygame.display.flip()
