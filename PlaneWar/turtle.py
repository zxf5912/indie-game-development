import pygame
from pygame import *
import sys

#初始化pygame
pygame.init()
#查看电脑支持的分辨率
print(pygame.display.list_modes())

size = width,height = 600,400
speed = [-2,1]
bg = (255,255,255) #背景色RGB

clock = pygame.time.Clock()

#创建指定大小的窗口，会返回一个Surface对象
screen = pygame.display.set_mode(size) #注意传入的size是:元组(宽,高)
#设置窗口标题
pygame.display.set_caption("初次见面，请大家多多关照！")

#加载图片
xiaobai = pygame.image.load("C:\\Users\\zxf\\Desktop\\haha.gif")
#获得图像的位置矩形
position = xiaobai.get_rect() #它应该是一个对象，然后有四个属性，left,right,top,bottom

l_head = xiaobai #将xiaobai本身设置成朝左的图
r_head = pygame.transform.flip(xiaobai,True,False) #将l_head翻转成朝右的图
fullscreen = False

while True: #循环
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        #当按下键盘
        if event.type == KEYDOWN:
            #判断是否按下<键
            if event.key == K_LEFT:
                #按下<键就将xiaobai刷成l_head
                xiaobai = l_head
                #调整x轴的运动方向为负，即令其向左移动
                speed = [-1,0]
            if event.key == K_RIGHT:
                xiaobai = r_head
                speed = [1,0]
            if event.key == K_UP:
                speed = [0,1]
            if event.key == K_DOWN:
                speed = [0,-1]

            #全屏(F11)

            if event.key == K_p:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((1024,768),FULLSCREEN | HWSURFACE)  #切换屏幕大小，进行FULLSCREEN全屏与HWSURFACE硬件加速

                else:
                    screen = pygame.display.set_mode(size) #切换回原来的屏幕大小


    #移动图像
    position = position.move(speed) #move方法，传入一个列表，[x,y]，代表像x方向移动的速度与向y方向移动的速度

    #碰撞检测
    if position.left < 0 or position.right > width:
        #翻转图像
        xiaobai = pygame.transform.flip(xiaobai,True,False) #flip(要翻转的对象,是否水平翻转,是否垂直翻转)
        #反方向移动
        speed[0] = -speed[0]

    if position.top < 0 or position.bottom > height:
        speed[1] = -speed[1]

    #填充背景
    screen.fill(bg)
    #更新图像，利用blit方法将xiaobai对象画到屏幕对象screen上去，画在哪画多大要看position
    screen.blit(xiaobai,position)
    #刷新界面，pygame使用的是双缓冲模式，所以要调用display.flip来将缓冲好的画面一次性刷新到显示器上，所谓双缓冲就是内存中有一个与Surface对象一样的对象
    #前面的fill和blit方法是写入内存中的对象中去，而flip是将内存中的对象一次性刷新到屏幕上，这样可以避免内存对象出一帧画面，写入到屏幕上一帧的这种情况，进而避免闪烁
    pygame.display.flip()
    #延迟10毫秒
    # pygame.time.delay(10)
    #控制帧率，不高于200帧每秒
    clock.tick(200)


