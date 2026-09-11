from tkinter import *

win = Tk()
win.geometry("669x634")
win.title("Weather")

Top_header = Frame(win,bg="#211C63",height = 130)
Top_header.pack(side = "top", fill = "x")
Main_body = Frame(win,bg="#197E27", height = 200)
Main_body.pack(side = "top", fill = "x")
Bottom = Frame(win,bg="#FFFFFF", height = 339)
Bottom.pack(side = "top", fill = "x")

space = Label(Top_header,bg="#211C63")
space.pack()
Title = Label(Top_header,text = "Weather App",font=("Impact",32), bg="#211C63",fg="white")
Title.pack()
space = Label(Top_header,bg="#211C63")
space.pack()

space = Label(Main_body,bg="#197E27")
space.pack()
Type_country = Entry(Main_body,bg="white",fg="grey",font=("Arial",20))
Type_country.pack()
space = Label(Main_body,bg="#197E27")
space.pack()
Search = Button(Main_body,text="Search",font=("Arial", 10),width=12,height=2)
Search.pack()
space = Label(Main_body,bg="#197E27")
space.pack()
space = Label(Main_body,bg="#197E27")
space.pack()

Temp = Label(Bottom,text="Temperature",bg="#F3F1F1",font=("Arial",20))
Temp.pack(side="top",fill="x")

win.mainloop()