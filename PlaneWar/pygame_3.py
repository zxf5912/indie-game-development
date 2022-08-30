import pygame
import sys

# 初始化pygame
pygame.init()

size = width, height = 600, 400
# 创建指定大小的窗口，会返回一个Surface对象
screen = pygame.display.set_mode(size)  # 注意传入的size是:元组(宽,高)
# 设置窗口标题
pygame.display.set_caption("My Demo")
bg = (0,0,0)
position = 0

#字体对象font
font = pygame.font.Font(None,20) #字体为None会选择默认字体，20是字号
line_height = font.get_linesize() #获取行高
screen.fill(bg) #填充背景为黑色

while True:  # 循环
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        screen.blit(font.render(str(event),True,(0,255,0)),(0,position)) #更新画面到sreen上，要更新的内容是(要渲染的文本，是否消除锯齿，(0,255,0)指的是纯绿色，最后是位置(0,position))
        position += line_height #position增加一个行高，也就是切换到下一行

        if position > height: #当超过行高时，就将position刷成0，将screen重新用黑色填充
            position = 0
            screen.fill(bg)

    pygame.display.flip() #刷新页面


