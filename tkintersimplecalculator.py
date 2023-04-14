from tkinter import *

def add():                           #Addition method 
    value1 = int(textbox1.get())
    value2 = int(textbox2.get())
    c= value1 + value2
    result.config(text="%d" % c)

def sub():                           #Subtraction method 
    value1 = int(textbox1.get())
    value2 = int(textbox2.get())
    c= value1 - value2
    result.config(text="%d" % c)

def mul():                            #multiplication method 
    value1 = int(textbox1.get())
    value2 = int(textbox2.get())
    c= value1 * value2
    result.config(text="%d" % c)


def div():                             #divition method 
    value1 = int(textbox1.get())
    value2 = int(textbox2.get())
    c= value1 / value2
    result.config(text="%d" % c)

def cl():

    textbox1.delete(0, END)
    textbox2.delete(0, END)

root = Tk()

root.geometry("200x250")

#lables ------------------------
lable1 = Label(root,text="value1")
lable1.grid(row=0, column=0,padx=5, pady=5, sticky=W)

lable2 = Label(root,text="value2")
lable2.grid(row=2, column=0,padx=5, pady=5,sticky=W)

result = Label(root,text="0",anchor=CENTER)
result.grid(row=4, column=0,columnspan=3,padx=5, pady=5)

#Textboxes ------------------------
textbox1 = Entry(root)
textbox1.grid(row=1, column=0,columnspan=3,padx=5, pady=5,sticky=W+E)

textbox2 = Entry(root)
textbox2.grid(row=3, column=0,columnspan=3,padx=5, pady=5,sticky=W+E)

#buttons ------------------------
addbutton = Button(root,text="Add",command=add)
addbutton.grid(row=5, column=0,padx=5, pady=5)

subbutton = Button(root,text="Subtract",command=sub)
subbutton.grid(row=5, column=1,padx=5, pady=5)

mulbutton = Button(root,text="Multiply" , command=mul)
mulbutton.grid(row=5, column=2,padx=5, pady=5)

divbutton = Button(root,text="Divide", command=div)
divbutton.grid(row=6, column=0,padx=5, pady=5)

clearbutton = Button(root,text="Clear", command=cl)
clearbutton.grid(row=6, column=2,padx=5, pady=5)

root.mainloop()

