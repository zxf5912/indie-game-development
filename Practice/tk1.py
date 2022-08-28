from tkinter import *

root = Tk() #设置一个窗口

textLabel = Label(root,text = "世界真美好！\n好好努力生活吧！") #在窗口中设置label，字样为“世界真美好”
textLabel.pack() #自动调整label位置


photo = PhotoImage(file= "C:\\Users\\zxf\\Desktop\\pikaqiu.gif") #读取图片
imgLabel = Label(root,image=photo) #一样的生成label，图像为photo
imgLabel.pack() #调整位置

mainloop() #循环main函数