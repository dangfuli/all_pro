# coding=utf-8
import tkinter
import sys
sys.path.append('/Users/dangfuli/Documents/PycharmProjects/all_pro/yxs-api/runner/')
from runner.runner import *
from tkinter import messagebox

class Loginwindow:
    def __init__(self):
        self.login = False
        self.root = tkinter.Tk()
        self.root.geometry("300x150-50-50")
        self.root.title('登录')
        self.textUserVar = tkinter.StringVar()
        self.textPswVar = tkinter.StringVar()

    def _checkout_login_status(self):
        if self.username.get() =='admin' and self.psw.get() == 'admin':
            self.login = True
            self.root.destroy()

        else:
            messagebox.askretrycancel(title='错误',message='账号密码错误，请重试！')

    def _quit_login(self):
        self.root.quit()

    def __save_userinfo(self):
        ##self.creat_user.get()
        ##self.creat_pswd.get()
        if self.creat_pswd.get() == self.creat_double_pswd.get():
            # 此处应该保存注册信息到数据库或者其他位置
            self.textUserVar.set(self.creat_user.get())
            self.textPswVar.set(self.creat_pswd.get())
            self.creat_top.destroy()
        else:
            messagebox.showerror(title='错误',message='两次输入密码不一致！请重试')

    def _create_user(self):
        # 在root顶部创建窗口
        self.creat_top = tkinter.Toplevel(self.root)
        self.creat_top.title('注册')
        self.creat_top.geometry('400x250')

        # 一些label文字信息
        tkinter.Label(self.creat_top,text='请输入注册信息',anchor='w').place(x=150,y=10)
        tkinter.Label(self.creat_top,text='用户名:',anchor='w').place(x=20,y=50)
        tkinter.Label(self.creat_top,text='密码:',anchor='w').place(x=20,y=100)
        tkinter.Label(self.creat_top,text='再次输入:',anchor='w').place(x=20,y=150)

        # 输入注册信息
        self.creat_user = tkinter.Entry(self.creat_top)
        self.creat_user.place(x=80,y=50)
        self.creat_pswd = tkinter.Entry(self.creat_top,show='*')
        self.creat_pswd.place(x=80,y=100)
        self.creat_double_pswd = tkinter.Entry(self.creat_top,show='*')
        self.creat_double_pswd.place(x=80,y=150)

        # 按钮
        tkinter.Button(self.creat_top,text='确认注册',command=self.__save_userinfo).place(x=120,y=200)

    def loginBuju(self):
        # 第一行是输入密码提示
        label1 = tkinter.Label(self.root,text='请输入用户名密码',anchor='center')
        label1.grid(row=0,column=1)
        # 用户名提示
        labelU = tkinter.Label(self.root,text='用户名:',anchor='w')
        labelU.grid(row=1,column=0)

        # 密码提示
        labelP = tkinter.Label(self.root,text='密码:',anchor='w')
        labelP.grid(row=2,column=0)

        # 输入框控件
        self.username = tkinter.Entry(self.root,textvariable=self.textUserVar)
        self.username.grid(row=1,column=1)
        self.psw = tkinter.Entry(self.root,show='*',textvariable=self.textPswVar)
        self.psw.grid(row=2,column=1)

        # 登录按钮
        loginButton = tkinter.Button(self.root,text='登录',command=self._checkout_login_status)
        loginButton.grid(row=4,column=2)

        # 注册按钮
        creatButton = tkinter.Button(self.root,text='注册',command=self._create_user)
        creatButton.grid(row=4,column=1)

        # 退出按钮
        quitButton = tkinter.Button(self.root,text='退出',command=self._quit_login)
        quitButton.grid(row=4,column=0)

        self.root.mainloop()

class Workwindow():
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("300x150")
        self.root.title('工作台')
        self.runVar = tkinter.StringVar()

    def _run_case(self):

        html_report()

    def workBuju(self):
        tkinter.Label(self.root,text='自动化控制台').place(x=100,y=10)
        self.runButton = tkinter.Button(self.root,text='悦小说api',command=self._run_case)
        self.runButton.place(x=20,y=30)

        self.runText = tkinter.Label(self.root,textvariable=self.runVar)
        self.runText.place(x=150,y=30)

        self.cancelButton = tkinter.Button(self.root,text='退出',command=lambda : self.root.quit())
        self.cancelButton.place(x=200,y=100)

        self.root.mainloop()


# l = Loginwindow()
# l.loginBuju()
#
# if l.login is True:
#     w = Workwindow()
#     w.workBuju()

w = Workwindow()
w.workBuju()
