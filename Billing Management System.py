#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import *
from tkinter import messagebox
import tempfile
import os

root=Tk()
root.title('Billing Manangement System')
root.geometry('1280x620+0+0')
bg_color='#2D9290'


#=====================variables===================
Bread=IntVar()
Biscuits=IntVar()
Wafers=IntVar()
Gal=IntVar()
Total=IntVar()

cb=StringVar()
cw=StringVar()
cr=StringVar()
cg=StringVar()
total_cost=StringVar()
# ===========Function===============
def total():
    if Bread.get()==0 and Biscuits.get()==0 and Wafers.get()==0 and Gal.get()==0:
        messagebox.showerror('Error','Please select number of quantity')
    else:
        b=Bread.get()
        w=Biscuits.get()
        r=Wafers.get()
        g=Gal.get()

        t=float(b*40.00 +w*10.00+r*120.00+g*12.00)
        Total.set(b + w + r + g)
        total_cost.set('Rs ' + str(round(t, 2)))

        cb.set('Rs.'+str(round(b*40.00,2)))
        cw.set('Rs.'+str(round(w*10.00,2)))
        cr.set('Rs.'+str(round(r*120.00,2)))
        cg.set('Rs.'+str(round(g*12.00,2)))






def receipt():
    textarea.delete(1.0,END)
    textarea.insert(END,' Items\tNumber of Items\t  Cost of Items\n')
    textarea.insert(END,f'\nBread\t\t{Bread.get()}\t  {cb.get()}')
    textarea.insert(END,f'\n\nBiscuits\t\t{Biscuits.get()}\t  {cw.get()}')
    textarea.insert(END,f'\n\nWafers\t\t{Wafers.get()}\t  {cr.get()}')
    textarea.insert(END,f'\n\nMilk\t\t{Gal.get()}\t  {cg.get()}')
    textarea.insert(END, f"\n\n================================")
    textarea.insert(END,f'\nTotal Price\t\t{Total.get()}\t{total_cost.get()}')
    textarea.insert(END, f"\n================================")


def print():
    q=textarea.get('1.0','end-1c')
    filename=tempfile.mktemp('.txt')
    open(filename,'w').write(q)
    os.startfile(filename,'Print')


def reset():
    textarea.delete(1.0,END)
    Bread.set(0)
    Biscuits.set(0)
    Wafers.set(0)
    Gal.set(0)
    Total.set(0)

    cb.set('')
    cw.set('')
    cr.set('')
    cg.set('')
    total_cost.set('')

def exit():
    if messagebox.askyesno('Exit','Do you really want to exit'):
        root.destroy()

#===============Product Details=================
F1 = LabelFrame(root, text='Product Details', font=('times new romon', 18, 'bold'), fg='gold',bg=bg_color,bd=15,relief=RIDGE)
F1.place(x=5, y=10,width=800,height=500)

#=====================Heading==========================
itm=Label(F1, text='Items', font=('Helvetic',25, 'bold','underline'), fg='black',bg=bg_color)
itm.grid(row=0,column=0,padx=20,pady=15)

n=Label(F1, text='Number of Items', font=('Helvetic',25, 'bold','underline'), fg='black',bg=bg_color)
n.grid(row=0,column=1,padx=30,pady=15)

cost=Label(F1, text='Cost of Items', font=('Helvetic',25, 'bold','underline'), fg='black',bg=bg_color)
cost.grid(row=0,column=2,padx=30,pady=15)

#===============Product============

bread=Label(F1, text='Bread', font=('times new rommon',20, 'bold'), fg='lawngreen',bg=bg_color)
bread.grid(row=1,column=0,padx=20,pady=15)
b_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=Bread,justify=CENTER)
b_txt.grid(row=1,column=1,padx=20,pady=15)
cb_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=cb,justify=CENTER)
cb_txt.grid(row=1,column=2,padx=20,pady=15)

biscuits=Label(F1, text='Biscuits', font=('times new rommon',20, 'bold'), fg='lawngreen',bg=bg_color)
biscuits.grid(row=2,column=0,padx=20,pady=15)
w_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=Biscuits,justify=CENTER)
w_txt.grid(row=2,column=1,padx=20,pady=15)
cw_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=cw,justify=CENTER)
cw_txt.grid(row=2,column=2,padx=20,pady=15)

wafers=Label(F1, text='Wafers', font=('times new rommon',20, 'bold'), fg='lawngreen',bg=bg_color)
wafers.grid(row=3,column=0,padx=20,pady=15)
r_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=Wafers,justify=CENTER)
r_txt.grid(row=3,column=1,padx=20,pady=15)
cr_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=cr,justify=CENTER)
cr_txt.grid(row=3,column=2,padx=20,pady=15)

gal=Label(F1, text='Milk', font=('times new rommon',20, 'bold'), fg='lawngreen',bg=bg_color)
gal.grid(row=4,column=0,padx=20,pady=15)
g_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=Gal,justify=CENTER)
g_txt.grid(row=4,column=1,padx=20,pady=15)
cg_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=cg,justify=CENTER)
cg_txt.grid(row=4,column=2,padx=20,pady=15)

t=Label(F1, text='Total', font=('times new rommon',20, 'bold'), fg='lawngreen',bg=bg_color)
t.grid(row=5,column=0,padx=20,pady=15)
t_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=Total,justify=CENTER)
t_txt.grid(row=5,column=1,padx=20,pady=15)
totalcost_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=total_cost,justify=CENTER)
totalcost_txt.grid(row=5,column=2,padx=20,pady=15)

#=====================Bill areea====================
F2=Frame(root,relief=GROOVE,bd=10)
F2.place(x=820,y=10,width=430,height=470)
bill_title=Label(F2,text='Receipt',font='arial 15 bold',bd=7,relief=GROOVE).pack(fill=X)
scrol_y=Scrollbar(F2,orient=VERTICAL)
scrol_y.pack(side=RIGHT,fill=Y)
textarea=Text(F2,font='arial 15',yscrollcommand=scrol_y.set)
textarea.pack(fill=BOTH)
scrol_y.config(command=textarea.yview)



#=====================Buttons========================
F3 =Frame(root,bg=bg_color,bd=15,relief=RIDGE)
F3.place(x=5, y=490,width=1270,height=130)

btn1 = Button(F3, text='Total', font='arial 25 bold', padx=5, pady=5, bg='yellow',fg='red',width=10,command=total)
btn1.grid(row=0,column=0,padx=20,pady=10)

btn2 = Button(F3, text='Receipt', font='arial 25 bold', padx=5, pady=5, bg='yellow',fg='red',width=10,command=receipt)
btn2.grid(row=0,column=1,padx=10,pady=10)

btn3 = Button(F3, text='Print', font='arial 25 bold', padx=5, pady=5, bg='yellow',fg='red',width=10,command=print)
btn3.grid(row=0,column=2,padx=10,pady=10)

btn4 = Button(F3, text='Reset', font='arial 25 bold', padx=5, pady=5, bg='yellow',fg='red',width=10,command=reset)
btn4.grid(row=0,column=3,padx=10,pady=10)

btn5 = Button(F3, text='Exit', font='arial 25 bold', padx=5, pady=5, bg='yellow',fg='red',width=10,command=exit)
btn5.grid(row=0,column=4,padx=10,pady=10)



root.mainloop()

