import tkinter
def add():
    e3.delete(0,"end")
    x=int(e1.get())
    y=int(e2.get())
    z=x+y
    e3.insert(0,str(z))
def sub():
    e3.delete(0, "end")
    x = int(e1.get())
    y = int(e2.get())
    z = x - y
    e3.insert(0, str(z))
def mul():
    e3.delete(0, "end")
    x = int(e1.get())
    y = int(e2.get())
    z = x * y
    e3.insert(0, str(z))
def div():
    e3.delete(0, "end")
    x = int(e1.get())
    y = int(e2.get())
    z = x // y
    e3.insert(0, str(z))
window=tkinter.Tk()
window.geometry("600x400")
window.title("Demo Window")
l1=tkinter.Label(text="enter first number")
l2=tkinter.Label(text="enter second number")
l3=tkinter.Label(text="Result")
e1=tkinter.Entry()
e2=tkinter.Entry()
e3=tkinter.Entry()
b1=tkinter.Button(text="add",command=add)
b2=tkinter.Button(text="sub",command=sub)
b3=tkinter.Button(text="mul",command=mul)
b4=tkinter.Button(text="div",command=div)
l1.place(x=100,y=100)
e1.place(x=230,y=100)
l2.place(x=100,y=150)
e2.place(x=230,y=150)
l3.place(x=100,y=200)
e3.place(x=230,y=200)
b1.place(x=100,y=250)
b2.place(x=200,y=250)
b3.place(x=300,y=250)
b4.place(x=400,y=250)
window.mainloop()
