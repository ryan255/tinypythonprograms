from tkinter import *
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import _thread
import sys

root = Tk()
root.title("ftpserver")

def run():
    _thread.start_new_thread ( ftpserver, ())

def exitftp():
    sys.exit(0)

def ftpserver():


    #实例化虚拟用户，这是FTP验证首要条件
    authorizer = DummyAuthorizer()

    #添加用户权限和路径，括号内的参数是(用户名， 密码， 用户目录， 权限)
    authorizer.add_user(var1.get(), var2.get(), '.', perm='elradfmw')

    #添加匿名用户 只需要路径
    authorizer.add_anonymous('.')

    #初始化ftp句柄
    handler = FTPHandler
    handler.authorizer = authorizer

    #监听ip 和 端口,因为linux里非root用户无法使用21端口，所以我使用了2121端口
    server = FTPServer((var3.get(), var4.get()), handler)

    #开始服务
    server.serve_forever()

#下面这些是对最开始的时候创建的tk进行行列式填充 label为文本 entry为输入框 
L1 = Label(root,text = 'UserName:').grid(column = 0,row = 0)
var1 = StringVar()
E1 = Entry(root,textvariable = var1, bd = 2).grid(column = 1,row = 0)
var1.set("admin")
user = var1.get()

L2 = Label(root,text = 'Password:').grid(column = 0,row = 1)
var2 = StringVar()
E2 = Entry(root,textvariable = var2, bd = 2).grid(column = 1,row = 1)
var2.set("123456")
password = var2.get()

L3 = Label(root,text = 'IP Address:').grid(column = 0,row = 2)
var3 = StringVar()
E3 = Entry(root,textvariable = var3, bd = 2).grid(column = 1,row = 2)
var3.set("0.0.0.0")
ipaddr = var3.get()

L4 = Label(root,text = 'PortNumber:').grid(column = 0,row = 3)
var4 = StringVar()
E4 = Entry(root,textvariable = var4, bd = 2).grid(column = 1,row = 3)
var4.set("2121")
port = var4.get()

Button1 = Button(root,text = "RunFtpserver",command=run).grid(column = 0,row = 4)
Button0 = Button(root,text = "Exit",command=exitftp).grid(column = 1,row = 4)
root.mainloop()