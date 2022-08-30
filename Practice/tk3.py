from tkinter import *

def callback(): #m没错就是我，我内置了var.set()函数，可以调用我来对变量var赋值
    var.set("bbb")

root = Tk() #生成窗口

frame1 = Frame(root) #第一个画面
frame2 = Frame(root) #第二个画面

var = StringVar() #该变量在这里
var.set("aaa") #对这个变量赋值为"aaa"

textLabel = Label(frame1, #对第一个画面进行设置
                  textvariable = var, #直接调用一个字符串的变量
                  justify=LEFT) #调整字体位置
textLabel.pack(side=LEFT)


photo = PhotoImage(file = "C:\\Users\\zxf\\Desktop\\haha.gif")
imgLabel = Label(frame1,image=photo)
imgLabel.pack(side = RIGHT)

theButton = Button(frame2,text="I'm Here.",fg="white",bg="black",command = callback) #fg是前景色，bg是后景色
#Button是按钮函数，前景是"I'm Here."字样，调用Button将会执行command，command执行的是callback函数

theButton.pack() #自适应调节我的Button位置

frame1.pack(padx=10,pady=10) #相对于x轴与y轴进行平移坐标，单位为10
frame2.pack(padx=10,pady=10)

mainloop()