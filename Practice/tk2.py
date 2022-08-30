from tkinter import *

root = Tk()

photo = PhotoImage(file= "C:\\Users\\zxf\\Desktop\\bg.gif")

theLabel = Label(root,
                 text = "Hi！\nCute World.", #字样
                 justify = LEFT, #文字位置
                 image=photo, #图像
                 compound=CENTER, #图像位置
                 font=("宋体",20), #字体与字号
                 fg="white") #前景色（前景就是文字，也就是文字颜色）

theLabel.pack() #自适应调整位置

mainloop() #执行mainloop