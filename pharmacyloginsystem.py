from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import time
import random
import datetime

def main():
    root = Tk()
    app = Window1(root)

class Window1:
    def login(self):
            user = self.username.get()
            pas = self.password.get()

            if (user==str(1234)) and (pas==str(2345)):
                self.btn1.configure(state=NORMAL)
                self.btn2.configure(state=NORMAL)

            else:
                tkinter.messagebox.askyesno("pharmacy","invalid data")
                self.btn1.configure(state=DISABLED)
                self.btn2.configure(state=DISABLED)
                self.username.set("")
                self.password.set("")
                self.txtusername.focus()

    def reset(self):
        self.btn1.configure(state=DISABLED)
        self.btn2.configure(state=DISABLED)
        self.username.set("")
        self.password.set("")
        self.txtusername.focus()

    def exits(self):
        self.exit = tkinter.messagebox.askyesno("pharmacy","Do you want to exit?")
        if self.exit > 0:
            self.master.destroy()
            return

                
    def __init__(self,master):
        self.master = master
        self.master.title("Pharmacy management system")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

        self.username = StringVar()
        self.password = StringVar()

        



        #===================frames============================================
        
        self.labeltitle = Label(self.frame,text="Pharmacy management system",
                                font=('arial',50,'bold'),bd=20)
        self.labeltitle.grid(row=0,column=0,columnspan=2,pady=20)

        self.frame1 = Frame(self.frame,width=1000,height=300,bd=20,relief='ridge')
        self.frame1.grid(row=1,column=0,pady=2)

        self.frame2 = Frame(self.frame,width=1000,height=100,bd=20,relief='ridge')
        self.frame2.grid(row=3,column=0)

        self.frame3 = Frame(self.frame,width=1000,height=200,bd=20,relief='ridge')
        self.frame3.grid(row=5,column=0,pady=2)

        #============================buttons=================================

        self.btn1 = Button(self.frame3,state=DISABLED,width=30,font=('arial',20,'bold'),command=self.win2,text="patient registration system")
        self.btn1.grid(row =0,column=0)

        self.btn2 = Button(self.frame3,state=DISABLED,width=30,font=('arial',20,'bold'),command=self.win3,text="hospital registration system")
        self.btn2.grid(row =0,column=2)

        self.btnlogin = Button(self.frame2,width=20,font=('arial',20,'bold'),command=self.login,text="Login")
        self.btnlogin.grid(row =0,column=0)

        self.btnreset = Button(self.frame2,width=20,font=('arial',20,'bold'),command=self.reset,text="Reset")
        self.btnreset.grid(row =0,column=1)

        self.btnexit = Button(self.frame2,width=20,font=('arial',20,'bold'),command=self.exits,text="Exit")
        self.btnexit.grid(row =0,column=2)

        self.lbusername = Label(self.frame1,text="Username",
                                font=('arial',30,'bold'),bd=20)
        self.lbusername.grid(row=0,column=0)

        self.txtusername = Entry(self.frame1,textvariable=self.username,
                                font=('arial',30,'bold'),bd=10)
        self.txtusername.grid(row=0,column=1)

        self.lbpassword = Label(self.frame1,text="Password",
                                font=('arial',30,'bold'),bd=20)
        self.lbpassword.grid(row=1,column=0)

        self.txtpassword = Entry(self.frame1,textvariable=self.password,
                                font=('arial',30,'bold'),bd=10)
        self.txtpassword.grid(row=1,column=1)

        #===============================================================

     



        



 


    def win2(self):
        self.newwindow = Toplevel(self.master)
        self.app = Window2(self.newwindow)

    def win3(self):
        self.newwindow = Toplevel(self.master)
        self.app = Window3(self.newwindow)

class Window2:
    def __init__(self,master):
        self.master = master
        self.master.title("patient registration system")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

class Window3:
    def __init__(self,master):
        self.master = master
        self.master.title("hospital management system")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()
        

if __name__ == '__main__':
    main()
