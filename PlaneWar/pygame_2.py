import pygame
import sys

#初始化pygame
pygame.init()

size = width,height = 600,400
#创建指定大小的窗口，会返回一个Surface对象
screen = pygame.display.set_mode(size) #注意传入的size是:元组(宽,高)
#设置窗口标题
pygame.display.set_caption("初次见面，请大家多多关照！")

f = open("record.txt",'w')

while True: #循环
    for event in pygame.event.get():

        f.write(str(event) + '\n')
        
        if event.type == pygame.QUIT:
            f.close()
            sys.exit()

