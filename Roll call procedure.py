#请在这里编写代码
#导入所需要的库
from tkinter import *
import random
#创建主窗口
root=Tk()
root.geometry('500x150+300+500')
root.title('点名系统')
#设置全局变量
var=StringVar()#这个标签用来显示标签上的名字
names=['汪居敬','陈奕潼','张靖德','倪正桐','徐启元','刘政远']
flag=False #这个标志用来表示是否正在进行点名
#定义一个函数，用来进行点名
def roll():
    if flag:#如果正在进行点名，那么显示一个随机的名字
        var.set(random.choice(names))
        root.after(10,roll)#在10毫秒后，再次调用函数
#定义一个函数，用来切换点名状态
def check():
    global flag #声明我们要使用的是全局变量，而不是穿件一个新的局部变量
    if flag:#如果正在进行点名，那么停止点名
        flag=False
    else:#否则，开始点名
        flag=True
        roll()
#创建并配置标签和按钮
Label(root,textvariable=var,font=('楷体',50)).pack()
Button(root,text="开始/停止点名",command=check).pack()
#启动事件循环
root.mainloop()
