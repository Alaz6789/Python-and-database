# pack,grid,place

from tkinter import *



win = Tk()
win.geometry("500x500")
win.title("Layout Manager App")


# FRAME
header = Frame(win,bg="grey",height=70)
header.pack(side="top",fill="x")


def doSomething(value):
    print("hello",value)

b1 = Button(header,text="home")
b1.pack(side=LEFT)
x = 10
b2 = Button(header,text="logout",command=lambda value=x:doSomething(value))
b2.pack(side=RIGHT)
b3 = Button(header,text="edit")
b3.pack(side=LEFT)
b4 = Button(header,text="file")
b4.pack(side=LEFT)
b5 = Button(header,text="selection")
b5.pack(side=LEFT)

footer = Frame(win,bg="orange",height=70)
footer.pack(side="bottom",fill="x")

l1 = Label(footer,text = "footer")
l1.pack()

Content = Frame(win,bg = 'red', height = 70)
Content.pack(side = 'left',fill=BOTH, expand=True)

l2 = Label(Content,bg = 'red')
l2.pack( )
l2 = Label(Content,bg = 'red')
l2.pack( )
l2 = Label(Content,bg = 'red')
l2.pack( )
l2 = Label(Content,bg = 'red')
l2.pack( )
l2 = Label(Content,bg = 'red')
l2.pack( )
l2 = Label(Content,bg = 'red')
l2.pack( )
l2 = Label(Content,bg = 'red')
l2.pack( )
l2 = Label(Content,bg = 'red')
l2.pack( )
l2 = Label(Content,bg = 'red')
l2.pack( )
l2 = Label(Content,bg = 'red')
l2.pack( )
l2 = Label(Content,text="Content")
l2.pack()











win.mainloop()