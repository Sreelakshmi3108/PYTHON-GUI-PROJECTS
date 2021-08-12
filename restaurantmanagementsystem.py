from tkinter import *
import random
import time


root=Tk()
root.geometry("1600x800+0+0")
root.title("restaurant")
txt=StringVar()
operator=""

tops=Frame(root,width=1600,height=50,bg="pink",relief=SUNKEN)
tops.pack(side=TOP)
f1=Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)
f2=Frame(root,width=300,height=700,bg="pink",relief=SUNKEN)
f2.pack(side=RIGHT)
#=============time===============
localtime=time.asctime(time.localtime(time.time()))
#==================info============================
lbinfo=Label(tops,font=('arial',50,'bold'),text="Restaurant management system",fg="steel blue",bd=10,anchor='w')
lbinfo.grid(row=0,column=0)
lbinfo1=Label(tops,font=('arial',20,'bold'),text=localtime,fg="steel blue",bd=10,anchor='w')
lbinfo1.grid(row=1,column=0)
#================calculator================
def btnclick(num):
    global operator
    operator=operator + str(num)
    txt.set(operator)

def btnclear():
    global operator
    operator=""
    txt.set("")

def equals():
    global operator
    total=str(eval(operator))
    txt.set(total)
    operator=""

def ref():
    x = random.randint(10090,39202)
    randomref = str(x)
    rand.set(randomref)

    cof = float(frie.get())
    coc = float(coke.get())
    cob = float(burger.get())
    cop = float(pasta.get())
    copi = float(pizza.get())
    cofr = float(frooti.get())

    costoffries = cof * 0.5
    costofcoke = coc * 0.78
    costofburger = cob * 0.7
    costofpasta = cop * 0.75
    costofpizza = copi * 0.9
    costoffrooti = cofr * 0.88

    costofmeal = "Rs." , str('%.2f' % (costoffries + costofcoke + costofburger +
                                     costofpasta + costofpizza + costoffrooti))
    ser = ((costoffries + costofcoke + costofburger +
             costofpasta + costofpizza + costoffrooti) /99)
    services = "Rs." , str('%.2f' % ser)
    taxs = ((costoffries + costofcoke + costofburger +
             costofpasta + costofpizza + costoffrooti)*0.1)
    sertax = "Rs." , str('%.2f' % taxs)
    totale = (costoffries + costofcoke + costofburger +
             costofpasta + costofpizza + costoffrooti) 
    subtotals = "Rs." , str('%.2f' % (totale + taxs))
    totals  = "Rs." , str('%.2f' % (totale + taxs + ser))

    cost.set(costofmeal)
    service.set(services)
    tax.set(sertax)
    subtotal.set(subtotals)
    total.set(totals)
    
                        
                                     
def exit():
    root.destroy()

def reset():
    rand.set("")
    frie.set("")
    coke.set("")
    burger.set("")
    pasta.set("")
    pizza.set("")
    frooti.set("")
    cost.set("")
    service.set("")
    tax.set("")
    subtotal.set("")
    total.set("")

    
txtdisplay=Entry(f2,font=('arial',20,'bold'),textvariable=txt,bd=30,insertwidth=4,
                 bg="powder blue",justify='left')
txtdisplay.grid(columnspan=4)

btn1=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="1",bg="powder blue",command=lambda:btnclick(1)).grid(row=2,column=0)

btn2=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="2",bg="powder blue",command=lambda:btnclick(2)).grid(row=2,column=1)
    
btn3=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="3",bg="powder blue",command=lambda:btnclick(3)).grid(row=2,column=2)

btn4=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="4",bg="powder blue",command=lambda:btnclick(4)).grid(row=3,column=0)

btn5=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="5",bg="powder blue",command=lambda:btnclick(5)).grid(row=3,column=1)

btn6=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="6",bg="powder blue",command=lambda:btnclick(6)).grid(row=3,column=2)

btn7=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="7",bg="powder blue",command=lambda:btnclick(7)).grid(row=4,column=0)

btn8=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="8",bg="powder blue",command=lambda:btnclick(8)).grid(row=4,column=1)

btn9=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="9",bg="powder blue",command=lambda:btnclick(9)).grid(row=4,column=2)

btn0=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="0",bg="powder blue",command=lambda:btnclick(0)).grid(row=5,column=0)


add=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="+",bg="powder blue",command=lambda:btnclick("+")).grid(row=2,column=3)

mul=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="*",bg="powder blue",command=lambda:btnclick("*")).grid(row=3,column=3)

sub=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="-",bg="powder blue",command=lambda:btnclick("-")).grid(row=4,column=3)

div=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="/",bg="powder blue",command=lambda:btnclick("/")).grid(row=5,column=3)

clear=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="C",bg="powder blue",command=btnclear).grid(row=5,column=1)

equalss=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="=",bg="powder blue",command=equals).grid(row=5,column=2)

#===============================info 1==================================

rand = StringVar()
frie = StringVar()
coke = StringVar()
burger = StringVar()
pasta = StringVar()
pizza = StringVar()

lbreference=Label(f1,font=('arial',16,'bold'),text="reference",bd=16,anchor='w')
lbreference.grid(row=0,column=0)
txtreference=Entry(f1,font=('arial',16,'bold'),textvariable=rand,bd=16,insertwidth=4,
                   bg="powder blue",justify='right')
txtreference.grid(row=0,column=1)

lbfries=Label(f1,font=('arial',16,'bold'),text="fries",bd=16,anchor='w')
lbfries.grid(row=1,column=0)
txtfries=Entry(f1,font=('arial',16,'bold'),textvariable=frie,bd=16,insertwidth=4,
                   bg="powder blue",justify='right')
txtfries.grid(row=1,column=1)

lbcoke=Label(f1,font=('arial',16,'bold'),text="coke",bd=16,anchor='w')
lbcoke.grid(row=2,column=0)
txtcoke=Entry(f1,font=('arial',16,'bold'),textvariable=coke,bd=16,insertwidth=4,
                   bg="powder blue",justify='right')
txtcoke.grid(row=2,column=1)

lbburger=Label(f1,font=('arial',16,'bold'),text="burger",bd=16,anchor='w')
lbburger.grid(row=3,column=0)
txtburger=Entry(f1,font=('arial',16,'bold'),textvariable=burger,bd=16,insertwidth=4,
                   bg="powder blue",justify='right')
txtburger.grid(row=3,column=1)

lbpasta=Label(f1,font=('arial',16,'bold'),text="pasta",bd=16,anchor='w')
lbpasta.grid(row=4,column=0)
txtpasta=Entry(f1,font=('arial',16,'bold'),textvariable=pasta,bd=16,insertwidth=4,
                   bg="powder blue",justify='right')
txtpasta.grid(row=4,column=1)

lbpizza=Label(f1,font=('arial',16,'bold'),text="pizza",bd=16,anchor='w')
lbpizza.grid(row=5,column=0)
txtpizza=Entry(f1,font=('arial',16,'bold'),textvariable=pizza,bd=16,insertwidth=4,
                   bg="powder blue",justify='right')
txtpizza.grid(row=5,column=1)

#===========================info 2 ========================================

frooti = StringVar()
cost = StringVar()
service = StringVar()
tax = StringVar()
subtotal = StringVar()
total = StringVar()

lbfrooti=Label(f1,font=('arial',16,'bold'),text="Frooti",bd=16,anchor='w')
lbfrooti.grid(row=0,column=2)
txtfrooti=Entry(f1,font=('arial',16,'bold'),textvariable=frooti,bd=16,insertwidth=4,
                   bg="powder blue",justify='right')
txtfrooti.grid(row=0,column=3)

lbcost=Label(f1,font=('arial',16,'bold'),text="Cost",bd=16,anchor='w')
lbcost.grid(row=1,column=2)
txtcost=Entry(f1,font=('arial',16,'bold'),textvariable=cost,bd=16,insertwidth=4,
                   bg="powder blue",justify='right')
txtcost.grid(row=1,column=3)

lbservice=Label(f1,font=('arial',16,'bold'),text="Service charge",bd=16,anchor='w')
lbservice.grid(row=2,column=2)
txtservice=Entry(f1,font=('arial',16,'bold'),textvariable=service,bd=16,insertwidth=4,
                   bg="powder blue",justify='right')
txtservice.grid(row=2,column=3)

lbtax=Label(f1,font=('arial',16,'bold'),text="state tax",bd=16,anchor='w')
lbtax.grid(row=3,column=2)
txttax=Entry(f1,font=('arial',16,'bold'),textvariable=tax,bd=16,insertwidth=4,
                   bg="powder blue",justify='right')
txttax.grid(row=3,column=3)

lbsubtotal=Label(f1,font=('arial',16,'bold'),text="Sub total",bd=16,anchor='w')
lbsubtotal.grid(row=4,column=2)
txtsubtotal=Entry(f1,font=('arial',16,'bold'),textvariable=subtotal,bd=16,insertwidth=4,
                   bg="powder blue",justify='right')
txtsubtotal.grid(row=4,column=3)

lbtotal=Label(f1,font=('arial',16,'bold'),text="Total cost",bd=16,anchor='w')
lbtotal.grid(row=5,column=2)
txttotal=Entry(f1,font=('arial',16,'bold'),textvariable=total,bd=16,insertwidth=4,
                   bg="powder blue",justify='right')
txttotal.grid(row=5,column=3)

#================btns=================================

btntotal=Button(f1,padx=16,pady=8,fg="black",font=('arial',16,'bold'),text="Total",
                bd=10,width=10,bg="powder blue",command=ref).grid(row=7,column=1)

btnreset=Button(f1,padx=16,pady=8,fg="black",font=('arial',16,'bold'),text="Reset",
                bd=10,width=10,bg="powder blue",command=reset).grid(row=7,column=2)

btnexit=Button(f1,padx=16,pady=8,fg="black",font=('arial',16,'bold'),text="Exit",
                bd=10,width=10,bg="powder blue",command=exit).grid(row=7,column=3)

root.mainloop()
