from tkinter import *

win = Tk()
win.geometry("300x400")
win.title("Calculator")

number = "0"

NumDisplay = Frame(win,bg="#222222",height = 130)
NumDisplay.pack(side="top",fill="x")
ButtonDisplay = Frame(win,bg="#222222",height = 290)
ButtonDisplay.pack(fill="x")
NumOnDisplay = Label(NumDisplay,text=number,font=("Arial",70),bg="#222222",fg="white")
NumOnDisplay.pack(side="right")

textGrid = [
     [7,8,9,'x'],
     [4,5,6,'+'],
     [1,2,3,'-'],
     [0,'.','del','/']  
     ]

def clearText():
    NumOnDisplay.config(text="0")

def inputText(value):
    ifTextis0 = NumOnDisplay.cget("text")
    for i in range(len(textGrid)):
     for j in range(len(textGrid[i])):
         if textGrid[i][j] == value:
             if ifTextis0 == "0":
                 NumOnDisplay.config(text="")
                 NumOnDisplay.config(text=str(NumOnDisplay.cget("text")) + str(value))
             else:
                 NumOnDisplay.config(text=str(NumOnDisplay.cget("text")) + str(value))

def calculate():
    NumString = NumOnDisplay.cget("text")
    for x in NumString:
        if x == "/":
            NumString = NumString.replace("/","//")
    for x in NumString:
        if x == "x":
            NumString = NumString.replace("x","*")
        if x == ".":
            NumString = NumString.replace("//","/")
    answer = eval(NumString)
    NumOnDisplay.config(text = str(answer))

attachedfun = None
for i in range(len(textGrid)):
     for j in range(len(textGrid[i])):
         if textGrid[i][j] == 'del':
             attachedfun = clearText
         else:
            attachedfun = lambda value=textGrid[i][j]:inputText(value)
         b = Button(ButtonDisplay,text=f"{textGrid[i][j]}",command=attachedfun,bg="#636262")
         b.grid(row=i,column=j,padx=2,pady=2,ipadx=25,ipady=14)

equal = Button(ButtonDisplay, text="enter",command= calculate,bg="#636262")
equal.grid(row=4,columnspan=6,padx=2,pady=2,ipadx=50,ipady=14)

win.mainloop()