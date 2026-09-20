import requests
from tkinter import *
import database as db
import settings as s

win = Tk()
win.geometry("669x850")
win.title("Dictionary")

Top_header = Frame(win,bg="#000000",height = 130)
Top_header.pack(side = "top", fill = "x")
Main_body = Frame(win,bg="#787878", height = 200)
Main_body.pack(side = "top", fill = "x")
Bottom = Frame(win,bg="#F3F1F1", height = 339)
Bottom.pack(side = "top", fill = "x")

space = Label(Top_header,bg="#000000")
space.pack()
Title = Label(Top_header,text = "My Dictionary",font=("Impact",32), bg="#000000",fg="white")
Title.pack()
space = Label(Top_header,bg="#000000")
space.pack()

space = Label(Main_body,bg="#787878")
space.pack()
Enter = Label(Main_body,text="Enter word:",bg="#787878",fg="white",font=("Arial",20,"bold"))
Enter.pack(side="top",fill="x")
space = Label(Main_body,bg="#787878")
space.pack()
Type_word = Entry(Main_body,bg="white",fg="grey",font=("Arial",20))
Type_word.pack()

def find_word():
    word = Type_word.get()

    db.validstatus(word)
    if s.status == True:
        data = db.find_word(word)
        temp = data[0]
        phonetics = data[1]
        speech = data[2]
        definitions = data[3]
        example = data[4]

    elif s.status == False:
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        res = requests.get(url)

        print(res.status_code)
        print(res.text)

        data = res.json()
        temp = data[0]['word']
        for phonetic in data[0]["phonetics"]:
            if "text" in phonetic:
                phonetics = phonetic["text"]
                break
        speech = data[0]['meanings'][0]['partOfSpeech']
        definitions = data[0]['meanings'][0]['definitions'][0]['definition']
        example = data[0]['meanings'][0]['definitions'][0].get("example","No example available")

        db.add_word(temp,phonetics,speech,definitions,example)

    Word.config(text=f"   Word:   {temp}")
    Phonetic.config(text=f"   Phonetic:   {phonetics}")
    Speech.config(text=f"   Part of speech:   {speech}")
    Definition.config(text=f"   {definitions}")
    Example.config(text=f"   {example}")

def search_history():
    data = db.search_history()
    num = len(data)
    if num == 0:
        Word.config(text="   You have no recorded searches")
        Phonetic.config(text="")
        Speech.config(text="")
        DefinitionWord.config(text="")
        Definition.config(text="")
        ExampleWord.config(text="")
        Example.config(text="")

    elif num == 1:
        Word.config(text="   Last search:")
        Phonetic.config(text=f"   {data[-1]}")
        Speech.config(text="")
        DefinitionWord.config(text="")
        Definition.config(text="")
        ExampleWord.config(text="")
        Example.config(text="")
        
    elif num == 2:
        Word.config(text="   Last 2 searches:")
        Phonetic.config(text=f"   {data[-1]}")
        Speech.config(text=f"   {data[-2]}")
        DefinitionWord.config(text="")
        Definition.config(text="")
        ExampleWord.config(text="")
        Example.config(text="")
        
    elif num == 3:
        Word.config(text="   Last 3 searches:")
        Phonetic.config(text=f"   {data[-1]}")
        Speech.config(text=f"   {data[-2]}")
        DefinitionWord.config(text=f"   {data[-3]}")
        Definition.config(text="")
        ExampleWord.config(text="")
        Example.config(text="")
        
    elif num == 4:
        Word.config(text="   Last 4 searches:")
        Phonetic.config(text=f"   {data[-1]}")
        Speech.config(text=f"   {data[-2]}")
        DefinitionWord.config(text=f"   {data[-3]}")
        Definition.config(text=f"   {data[-4]}")
        ExampleWord.config(text="")
        Example.config(text="")
        
    elif num >= 5:
        Word.config(text="   Last 5 searches:")
        Phonetic.config(text=f"   {data[-1]}")
        Speech.config(text=f"   {data[-2]}")
        DefinitionWord.config(text=f"   {data[-3]}")
        Definition.config(text=f"   {data[-4]}")
        ExampleWord.config(text=f"   {data[-5]}")
        Example.config(text="")

space = Label(Main_body,bg="#787878")
space.pack()
buttonFrame = Frame(Main_body,bg="#787878")
buttonFrame.pack()
SearchHistory = Button(buttonFrame,text="Search history",font=("Arial", 10),width=12,height=2,command=search_history)
SearchHistory.pack(side=LEFT,padx=20)
Search = Button(buttonFrame,text="Search",font=("Arial", 10),width=12,height=2,command=find_word)
Search.pack(side=LEFT,padx=20)
DeleteHistory = Button(buttonFrame,text="Delete history",font=("Arial", 10),width=12,height=2,command=db.Delete_history)
DeleteHistory.pack(side=LEFT,padx=20)
space = Label(Main_body,bg="#787878")
space.pack()
space = Label(Main_body,bg="#787878")
space.pack()


Word = Label(Bottom,text="   Word:   ------",bg="#F3F1F1",font=("Arial",20))
Word.pack(anchor="w", pady = 10)

Phonetic = Label(Bottom,text="   Phonetic:   ------",bg="#F3F1F1",font=("Arial",20))
Phonetic.pack(anchor="w", pady = 10)

Speech = Label(Bottom,text="   Part of speech:   ------",bg="#F3F1F1",font=("Arial",20))
Speech.pack(anchor="w", pady = 10)

DefinitionWord = Label(Bottom,text="   Definition:",bg="#F3F1F1",font=("Arial",20))
DefinitionWord.pack(anchor="w", pady = 10)
Definition = Label(Bottom,text="   ------:",bg="#F3F1F1",font=("Arial",20))
Definition.pack(anchor="w", pady = 10)

ExampleWord = Label(Bottom,text="   Example:",bg="#F3F1F1",font=("Arial",20))
ExampleWord.pack(anchor="w", pady = 10)
Example = Label(Bottom,text="   ------",bg="#F3F1F1",font=("Arial",20))
Example.pack(anchor="w", pady = 10)


win.mainloop()