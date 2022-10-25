import tkinter
def display():
    x=i.get()
    if x==1:
        window.config(bg="Red")
    elif x==2:
        window.config(bg="Green")
    else:
        window.config(bg="Blue")
window=tkinter.Tk()
window.geometry("600x400")
window.title("Demo window")
i=tkinter.IntVar()
rb1=tkinter.Radiobutton(text="Red",variable=i,value=1,command=display)
rb2=tkinter.Radiobutton(text="Green",variable=i,value=2,command=display)
rb3=tkinter.Radiobutton(text="Blue",variable=i,value=3,command=display)
rb1.place(x=100,y=100)
rb2.place(x=200,y=100)
rb3.place(x=300,y=100)
window.mainloop()