from tkinter import *
from tkinter import messagebox
import random
import time
import datetime
from tkinter import Tk, StringVar, ttk

root=Tk()
root.geometry("1350x750+50+25")
root.title("Fast food restaurant")

Tops = Frame(root,width=1350,height=100,bd=12,relief="raise")
Tops.pack(side=TOP)
lbtitle = Label(Tops,font=('arial',50,'bold'),text="\tFast Food Restaurant\t\t\t")
lbtitle.grid(row=0,column=0)

Bottomframe = Frame(root,width=1350,height=650,bd=12,relief="raise")
Bottomframe.pack(side=BOTTOM)

f1 = Frame(Bottomframe,width=450,height=650,bd=12,relief="raise")
f1.pack(side=LEFT)

f2 = Frame(Bottomframe,width=450,height=650,bd=12,relief="raise")
f2.pack(side=LEFT)
f2top = Frame(f2,width=450,height=350,bd=6,relief="raise")
f2top.pack(side=TOP)
f2bottom = Frame(f2,width=450,height=300,bd=6,relief="raise")
f2bottom.pack(side=BOTTOM)


f3 = Frame(Bottomframe,width=450,height=650,bd=12,relief="raise")
f3.pack(side=RIGHT)

#=======================================================

def qexit():
    iexit = messagebox.askyesno("Fast food","Do you want to quit")
    if iexit>0:
        root.destroy()
        return

def reset():
    varfries.set("0")
    varsalad.set("0")
    varburger.set("0")
    varrings.set("0")
    varsandwich.set("0")
    varpasta.set("0")
    varpizza.set("0")
    varchips.set("0")
    varpan.set("0")
    varmuffin.set("0")
    varbagel.set("0")
    varcake.set("0")
    vardoughnut.set("0")
    varchange.set("0")
    vartax.set("0")
    varsubtotal.set("0")
    vartotal.set("0")
    varpayment.set("")
    vartea.set("0")
    varcola.set("0")
    varcoffee.set("0")
    varorange.set("0")
    varwater.set("0")
    varcone.set("0")
    varshake.set("0")
    varstrawberry.set("0")

    txtfries.configure(state=DISABLED)
    txtsalad.configure(state=DISABLED)
    txtburger.configure(state=DISABLED)
    txtrings.configure(state=DISABLED)
    txtpasta.configure(state=DISABLED)
    txtpizza.configure(state=DISABLED)
    txtsandwich.configure(state=DISABLED)
    txtchips.configure(state=DISABLED)
    txtpan.configure(state=DISABLED)
    txtmuffin.configure(state=DISABLED)
    txtbagel.configure(state=DISABLED)
    txtdoughnut.configure(state=DISABLED)
    txtcake.configure(state=DISABLED)
    txtchange.configure(state=DISABLED)
    txtsubtotal.configure(state=DISABLED)
    txttax.configure(state=DISABLED)
    txttotal.configure(state=DISABLED)
    txttea.configure(state=DISABLED)
    txtcola.configure(state=DISABLED)
    txtcoffee.configure(state=DISABLED)
    txtshake.configure(state=DISABLED)
    txtvanilla.configure(state=DISABLED)
    txtorange.configure(state=DISABLED)
    txtwater.configure(state=DISABLED)
    txtstrawberry.configure(state=DISABLED)

def chkfries():
    if(var1.get()==1):
        txtfries.configure(state=NORMAL)
        varfries.set("")
    elif(var1.get()==0):
        txtfries.configure(state=DISABLED)
        varfries.set("0")

def chksalad():
    if(var2.get()==1):
        txtsalad.configure(state=NORMAL)
        varsalad.set("")
    elif(var2.get()==0):
        txtsalad.configure(state=DISABLED)
        varsalad.set("0")

def chkburger():
    if(var3.get()==1):
        txtburger.configure(state=NORMAL)
        varburger.set("")
    elif(var3.get()==0):
        txtburger.configure(state=DISABLED)
        varburger.set("0")

def chkrings():
    if(var4.get()==1):
        txtrings.configure(state=NORMAL)
        varrings.set("")
    elif(var4.get()==0):
        txtrings.configure(state=DISABLED)
        varrings.set("0")

def chksandwich():
    if(var5.get()==1):
        txtsandwich.configure(state=NORMAL)
        varsandwich.set("")
    elif(var5.get()==0):
        txtsandwich.configure(state=DISABLED)
        varsandwich.set("0")

def chkpasta():
    if(var6.get()==1):
        txtpasta.configure(state=NORMAL)
        varpasta.set("")
    elif(var6.get()==0):
        txtpasta.configure(state=DISABLED)
        varpasta.set("0")

def chkpizza():
    if(var7.get()==1):
        txtpizza.configure(state=NORMAL)
        varpizza.set("")
    elif(var7.get()==0):
        txtpizza.configure(state=DISABLED)
        varpizza.set("0")

def chkchips():
    if(var8.get()==1):
        txtchips.configure(state=NORMAL)
        varchips.set("")
    elif(var8.get()==0):
        txtchips.configure(state=DISABLED)
        varchips.set("0")

def chkpan():
    if(var9.get()==1):
        txtpan.configure(state=NORMAL)
        varpan.set("")
    elif(var9.get()==0):
        txtpan.configure(state=DISABLED)
        varpan.set("0")

def chkmuffin():
    if(var10.get()==1):
        txtmuffin.configure(state=NORMAL)
        varmuffin.set("")
    elif(var10.get()==0):
        txtmuffin.configure(state=DISABLED)
        varmuffin.set("0")

def chkbagel():
    if(var11.get()==1):
        txtbagel.configure(state=NORMAL)
        varbagel.set("")
    elif(var11.get()==0):
        txtbagel.configure(state=DISABLED)
        varbagel.set("0")

def chkcake():
    if(var12.get()==1):
        txtcake.configure(state=NORMAL)
        varcake.set("")
    elif(var12.get()==0):
        txtcake.configure(state=DISABLED)
        varcake.set("0")

def chkdoughnut():
    if(var13.get()==1):
        txtdoughnut.configure(state=NORMAL)
        vardoughnut.set("")
    elif(var13.get()==0):
        txtdoughnut.configure(state=DISABLED)
        vardoughnut.set("0")

def chktea():
    if(var15.get()==1):
        txttea.configure(state=NORMAL)
        vartea.set("")
    elif(var15.get()==0):
        txttea.configure(state=DISABLED)
        vartea.set("0")

def chkcola():
    if(var16.get()==1):
        txtcola.configure(state=NORMAL)
        varcola.set("")
    elif(var16.get()==0):
        txtcola.configure(state=DISABLED)
        varcola.set("0")

def chkcoffee():
    if(var17.get()==1):
        txtcoffee.configure(state=NORMAL)
        varcoffee.set("")
    elif(var17.get()==0):
        txtcoffee.configure(state=DISABLED)
        varcoffee.set("0")

def chkorange():
    if(var18.get()==1):
        txtorange.configure(state=NORMAL)
        varorange.set("")
    elif(var18.get()==0):
        txtorange.configure(state=DISABLED)
        varorange.set("0")

def chkwater():
    if(var19.get()==1):
        txtwater.configure(state=NORMAL)
        varwater.set("")
    elif(var19.get()==0):
        txtwater.configure(state=DISABLED)
        varwater.set("0")

def chkcone():
    if(var20.get()==1):
        txtvanilla.configure(state=NORMAL)
        varcone.set("")
    elif(var20.get()==0):
        txtvanilla.configure(state=DISABLED)
        varcone.set("0")

def chkshake():
    if(var21.get()==1):
        txtshake.configure(state=NORMAL)
        varshake.set("")
    elif(var21.get()==0):
        txtshake.configure(state=DISABLED)
        varshake.set("0")

def chkstrawberry():
    if(var22.get()==1):
        txtstrawberry.configure(state=NORMAL)
        varstrawberry.set("")
    elif(var22.get()==0):
        txtstrawberry.configure(state=DISABLED)
        varstrawberry.set("0")

def total():
    meal1 = float(varfries.get())
    meal2 = float(varsalad.get())
    meal3 = float(varburger.get())
    meal4 = float(varrings.get())
    meal5 = float(varsandwich.get())
    meal6 = float(varpasta.get())
    meal7 = float(varpizza.get())
    meal8 = float(varchips.get())
    meal9 = float(varpan.get())
    meal10 = float(varmuffin.get())
    meal11 = float(varbagel.get())
    meal12 = float(varcake.get())
    meal13 = float(vardoughnut.get())
    meal14 = float(vartea.get())
    meal15 = float(varcola.get())
    meal16 = float(varcoffee.get())
    meal17 = float(varorange.get())
    meal18 = float(varwater.get())
    meal19 = float(varcone.get())
    meal20 = float(varshake.get())
    meal21 = float(varstrawberry.get())

    itotal1 = ((meal1*1) + (meal2*1) + (meal3*1) + (meal4*1))
    itotal2 = ((meal5*1) + (meal6*1) + (meal7*1) + (meal8*1))
    itotal3 = ((meal9*1) + (meal10*1) + (meal11*1) + (meal12*1))
    itotal4 = ((meal13*1) + (meal14*1) + (meal15*1) + (meal16*1))
    itotal5 = ((meal17*1) + (meal18*1) + (meal19*1) + (meal20*1) + (meal21*1))

    

    if(cmbpay.get()=="cash"):
        ichange = float(varpayment.get())
        isubtotal = (itotal1 + itotal2 + itotal3 + itotal4 + itotal5)
        isubtotalq = "Rs.",str("%.2f" % (isubtotal))
        itax = (isubtotal*0.1)
        itaxq = "Rs.",str("%.2f" % (itax))
        itotalq = "Rs.",str("%.2f" % (itax + isubtotal))
        rchange = (ichange - (itax + isubtotal))
        ichangeq = "Rs.",str("%.2f" % (rchange))
        varchange.set(ichangeq)
        varsubtotal.set(isubtotalq)
        vartax.set(itaxq)
        vartotal.set(itotalq)

    elif(cmbpay.get()=="master card" or "visa card" or "debit card"):
        varpayment.set("")
        isubtotal = (itotal1 + itotal2 + itotal3 + itotal4 + itotal5)
        itax = (isubtotal*0.1)
        itaxq = "Rs.",str("%.2f" % (itax))
        isubtotalq = "Rs.",str("%.2f" % (isubtotal))
        itotalq = "Rs.",str("%.2f" % (itax + isubtotal))
        varsubtotal.set(isubtotalq)
        vartax.set(itaxq)
        vartotal.set(itotalq)
        varchange.set("")



#=====================f1======================================

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var22 = IntVar()
var23 = IntVar()

var1.set(0)
var2.set(0)
var3.set(0)
var4.set(0)
var5.set(0)
var6.set(0)
var7.set(0)
var8.set(0)
var9.set(0)
var10.set(0)
var11.set(0)
var12.set(0)
var13.set(0)
var14.set(0)
var15.set(0)
var16.set(0)
var17.set(0)
var18.set(0)
var19.set(0)
var20.set(0)
var21.set(0)
var22.set(0)
var23.set(0)

varfries = StringVar()
varsalad = StringVar()
varburger = StringVar()
varrings = StringVar()
varsandwich = StringVar()
varpasta = StringVar()
varpizza = StringVar()
varchips = StringVar()
varrolls = StringVar()

varfries.set("0")
varsalad.set("0")
varburger.set("0")
varrings.set("0")
varsandwich.set("0")
varpasta.set("0")
varpizza.set("0")
varchips.set("0")


lblabel = Label(f1,font=('arial',18,'bold'),text="\tFast Food\n")
lblabel.grid(row=0,column=0)

fries = Checkbutton(f1,text="Fries",variable=var1,onvalue=1,offvalue=0,
                    font=('arial',18,'bold'),command=chkfries).grid(row=1,column=0,sticky=W)
txtfries = Entry(f1,font=('arial',18,'bold'),textvariable=varfries,width=8,
                 state=DISABLED,justify='left')
txtfries.grid(row=1,column=1)

salad = Checkbutton(f1,text="Salad",variable=var2,onvalue=1,offvalue=0,
                    font=('arial',18,'bold'),command=chksalad).grid(row=2,column=0,sticky=W)
txtsalad = Entry(f1,font=('arial',18,'bold'),textvariable=varsalad,width=8,
                 state=DISABLED,justify='left')
txtsalad.grid(row=2,column=1)

burger = Checkbutton(f1,text="Burger",variable=var3,onvalue=1,offvalue=0,
                    font=('arial',18,'bold'),command=chkburger).grid(row=3,column=0,sticky=W)
txtburger = Entry(f1,font=('arial',18,'bold'),textvariable=varburger,width=8,
                 state=DISABLED,justify='left')
txtburger.grid(row=3,column=1)

onionrings = Checkbutton(f1,text="Onion Rings",variable=var4,onvalue=1,offvalue=0,
                    font=('arial',18,'bold'),command=chkrings).grid(row=4,column=0,sticky=W)
txtrings = Entry(f1,font=('arial',18,'bold'),textvariable=varrings,width=8,
                 state=DISABLED,justify='left')
txtrings.grid(row=4,column=1)


sandwich = Checkbutton(f1,text="Sandwich",variable=var5,onvalue=1,offvalue=0,
                    font=('arial',18,'bold'),command=chksandwich).grid(row=5,column=0,sticky=W)
txtsandwich = Entry(f1,font=('arial',18,'bold'),textvariable=varsandwich,width=8,
                 state=DISABLED,justify='left')
txtsandwich.grid(row=5,column=1)

pasta = Checkbutton(f1,text="Pasta",variable=var6,onvalue=1,offvalue=0,
                    font=('arial',18,'bold'),command=chkpasta).grid(row=6,column=0,sticky=W)
txtpasta = Entry(f1,font=('arial',18,'bold'),textvariable=varpasta,width=8,
                 state=DISABLED,justify='left')
txtpasta.grid(row=6,column=1)

pizza = Checkbutton(f1,text="Pizza",variable=var7,onvalue=1,offvalue=0,
                    font=('arial',18,'bold'),command=chkpizza).grid(row=7,column=0,sticky=W)
txtpizza = Entry(f1,font=('arial',18,'bold'),textvariable=varpizza,width=8,
                 state=DISABLED,justify='left')
txtpizza.grid(row=7,column=1)

chips = Checkbutton(f1,text="Chips",variable=var8,onvalue=1,offvalue=0,
                    font=('arial',18,'bold'),command=chkchips).grid(row=8,column=0,sticky=W)
txtchips = Entry(f1,font=('arial',18,'bold'),textvariable=varchips,width=8,
                 state=DISABLED,justify='left')
txtchips.grid(row=8,column=1)

lbspace = Label(f1,text="\n\n\n\n\n\n\n\n\n\n\n\n")
lbspace.grid(row=9,column=0)

#==============================f2top===========================

varpan = StringVar()
varmuffin = StringVar()
varbagel = StringVar()
varcake = StringVar()
vardoughnut = StringVar()

varpan.set("0")
varmuffin.set("0")
varbagel.set("0")
varcake.set("0")
vardoughnut.set("0")

lblabel1 = Label(f2top,font=('arial',18,'bold'),text="\tDeserts\t\t\t\n")
lblabel1.grid(row=0,column=0)

pancake = Checkbutton(f2top,text="Pancake\t\t",variable=var9,onvalue=1,offvalue=0,
                    font=('arial',18,'bold'),command=chkpan).grid(row=1,column=0,sticky=W)
txtpan= Entry(f2top,font=('arial',18,'bold'),textvariable=varpan,width=8,
                 state=DISABLED,justify='left')
txtpan.grid(row=1,column=1)

muffin = Checkbutton(f2top,text="Chocolate Muffin",variable=var10,onvalue=1,offvalue=0,
                    font=('arial',18,'bold'),command=chkmuffin).grid(row=2,column=0,sticky=W)
txtmuffin = Entry(f2top,font=('arial',18,'bold'),textvariable=varmuffin,width=8,
                 state=DISABLED,justify='left')
txtmuffin.grid(row=2,column=1)

bagel = Checkbutton(f2top,text="Bagel",variable=var11,onvalue=1,offvalue=0,
                    font=('arial',18,'bold'),command=chkbagel).grid(row=3,column=0,sticky=W)
txtbagel = Entry(f2top,font=('arial',18,'bold'),textvariable=varbagel,width=8,
                 state=DISABLED,justify='left')
txtbagel.grid(row=3,column=1)

cake = Checkbutton(f2top,text="Cake",variable=var12,onvalue=1,offvalue=0,
                    font=('arial',18,'bold'),command=chkcake).grid(row=4,column=0,sticky=W)
txtcake = Entry(f2top,font=('arial',18,'bold'),textvariable=varcake,width=8,
                 state=DISABLED,justify='left')
txtcake.grid(row=4,column=1)

doughnut = Checkbutton(f2top,text="Doughnut",variable=var13,onvalue=1,offvalue=0,
                    font=('arial',18,'bold'),command=chkdoughnut).grid(row=5,column=0,sticky=W)
txtdoughnut = Entry(f2top,font=('arial',18,'bold'),textvariable=vardoughnut,width=8,
                 state=DISABLED,justify='left')
txtdoughnut.grid(row=5,column=1)

lbspace = Label(f2top,text="\n\n")
lbspace.grid(row=6,column=0)



#====================f2bottom=========================

varchange = StringVar()
vartax = StringVar()
varsubtotal = StringVar()
vartotal = StringVar()
varpayment = StringVar()

varchange.set("0")
vartax.set("0")
varsubtotal.set("0")
vartotal.set("0")
varpayment.set("")

lblabel2 = Label(f2bottom,font=('arial',18,'bold'),text="Payment Method")
lblabel2.grid(row=0,column=0)

lbchange = Label(f2bottom,font=('arial',18,'bold'),text="Change",bd=10,anchor='w')
lbchange.grid(row=0,column=1)
txtchange= Entry(f2bottom,font=('arial',18,'bold'),textvariable=varchange,width=8,
                 state=DISABLED,justify='left')
txtchange.grid(row=0,column=2)

cmbpay = ttk.Combobox(f2bottom,font=('arial',18,'bold'),textvariable=var14,
                      state='readonly')
cmbpay['value']=('cash','master card','visa card','debitcard')
cmbpay.current(0)
cmbpay.grid(row=1,column=0)

txtpayment= Entry(f2bottom,font=('arial',18,'bold'),textvariable=varpayment,width=5,
                 justify='left').grid(row=2,column=0)

lbtax = Label(f2bottom,font=('arial',18,'bold'),text="Tax",bd=10,anchor='w')
lbtax.grid(row=1,column=1)
txttax= Entry(f2bottom,font=('arial',18,'bold'),textvariable=vartax,width=8,
                 state=DISABLED,justify='left')
txttax.grid(row=1,column=2)

lbsubtotal = Label(f2bottom,font=('arial',18,'bold'),text="Subtotal",bd=10,anchor='w')
lbsubtotal.grid(row=2,column=1)
txtsubtotal= Entry(f2bottom,font=('arial',18,'bold'),textvariable=varsubtotal,width=8,
                 state=DISABLED,justify='left')
txtsubtotal.grid(row=2,column=2)

lbtotal = Label(f2bottom,font=('arial',18,'bold'),text="Total",bd=10,anchor='w')
lbtotal.grid(row=3,column=1)
txttotal= Entry(f2bottom,font=('arial',18,'bold'),textvariable=vartotal,width=8,
                 state=DISABLED,justify='left')
txttotal.grid(row=3,column=2)

#====================f2bottombtns=======================

btntotal = Button(f2bottom,fg="black",font=('arial',16,'bold'),
                  width=5,text="Total",command=total).grid(row=5,column=0)

btnreset = Button(f2bottom,fg="black",font=('arial',16,'bold'),
                  width=5,text="Reset",command=reset).grid(row=5,column=1)

btnexit = Button(f2bottom,fg="black",font=('arial',16,'bold'),
                  width=5,text="Exit",command=qexit).grid(row=5,column=2)

#===========================f3==============================

vartea = StringVar()
varcola = StringVar()
varcoffee = StringVar()
varorange = StringVar()
varwater = StringVar()
varcone = StringVar()
varshake = StringVar()
varstrawberry = StringVar()

vartea.set("0")
varcola.set("0")
varcoffee.set("0")
varorange.set("0")
varwater.set("0")
varcone.set("0")
varshake.set("0")
varstrawberry.set("0")

lblabel = Label(f3,font=('arial',18,'bold'),text="\tDrinks\n")
lblabel.grid(row=0,column=0)

tea = Checkbutton(f3,text="Tea",variable=var15,onvalue=1,offvalue=0,
                    font=('arial',18,'bold'),command=chktea).grid(row=1,column=0,sticky=W)
txttea = Entry(f3,font=('arial',18,'bold'),textvariable=vartea,width=8,
                 state=DISABLED,justify='left')
txttea.grid(row=1,column=1)

cola = Checkbutton(f3,text="Cola",variable=var16,onvalue=1,offvalue=0,
                    font=('arial',18,'bold'),command=chkcola).grid(row=2,column=0,sticky=W)
txtcola = Entry(f3,font=('arial',18,'bold'),textvariable=varcola,width=8,
                 state=DISABLED,justify='left')
txtcola.grid(row=2,column=1)

coffee = Checkbutton(f3,text="Coffee",variable=var17,onvalue=1,offvalue=0,
                    font=('arial',18,'bold'),command=chkcoffee).grid(row=3,column=0,sticky=W)
txtcoffee = Entry(f3,font=('arial',18,'bold'),textvariable=varcoffee,width=8,
                 state=DISABLED,justify='left')
txtcoffee.grid(row=3,column=1)

orange = Checkbutton(f3,text="Orange",variable=var18,onvalue=1,offvalue=0,
                    font=('arial',18,'bold'),command=chkorange).grid(row=4,column=0,sticky=W)
txtorange = Entry(f3,font=('arial',18,'bold'),textvariable=varorange,width=8,
                 state=DISABLED,justify='left')
txtorange.grid(row=4,column=1)


water = Checkbutton(f3,text="Water",variable=var19,onvalue=1,offvalue=0,
                    font=('arial',18,'bold'),command=chkwater).grid(row=5,column=0,sticky=W)
txtwater = Entry(f3,font=('arial',18,'bold'),textvariable=varwater,width=8,
                 state=DISABLED,justify='left')
txtwater.grid(row=5,column=1)

lblabel1 = Label(f3,font=('arial',18,'bold'),text="\tShakes\n")
lblabel1.grid(row=6,column=0)


vanilla = Checkbutton(f3,text="Vanilla cone",variable=var20,onvalue=1,offvalue=0,
                    font=('arial',18,'bold'),command=chkcone).grid(row=7,column=0,sticky=W)
txtvanilla = Entry(f3,font=('arial',18,'bold'),textvariable=varcone,width=8,
                 state=DISABLED,justify='left')
txtvanilla.grid(row=7,column=1)

shake = Checkbutton(f3,text="Vanilla shake",variable=var21,onvalue=1,offvalue=0,
                    font=('arial',18,'bold'),command=chkshake).grid(row=8,column=0,sticky=W)
txtshake = Entry(f3,font=('arial',18,'bold'),textvariable=varshake,width=8,
                 state=DISABLED,justify='left')
txtshake.grid(row=8,column=1)

strawberry= Checkbutton(f3,text="Strawberry shake",variable=var22,onvalue=1,offvalue=0,
                    font=('arial',18,'bold'),command=chkstrawberry).grid(row=9,column=0,sticky=W)
txtstrawberry = Entry(f3,font=('arial',18,'bold'),textvariable=varstrawberry,width=8,
                 state=DISABLED,justify='left')
txtstrawberry.grid(row=9,column=1)

lbspace = Label(f3,text="\n\n\n\n\n\n\n\n\n\n\n\n")
lbspace.grid(row=10,column=0)















root.mainloop()
