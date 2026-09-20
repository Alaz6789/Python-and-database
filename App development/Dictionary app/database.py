import sqlite3
import settings as s

dictionaryDatabase = sqlite3.connect("Dictionary database.db")
dictionaryCursor = dictionaryDatabase.cursor()

dictionaryCursor.execute("""create table if not exists dictionary(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        word TEXT,
                        phonetic TEXT,
                        part_of_speech TEXT,
                        definition TEXT,
                        example TEXT
                        )""")

def add_word(word, phonetic, part_of_speech, definition, example):
    dictionaryCursor.execute('''
            insert into dictionary(word, phonetic, part_of_speech, definition, example) values(?,?,?,?,?)
            ''',(word, phonetic, part_of_speech, definition, example))
    print("Word added successfully!")
    dictionaryDatabase.commit()

def validstatus(word):
    validstatus = dictionaryCursor.execute('''
                    select * from dictionary where word == ?
                    ''',(word,))
    if validstatus.fetchone():
        print("This word is in the database.")
        s.status = True
        return
    else:
        print("This word is NOT in the database.")
        s.status = False

def find_word(word):
    data = dictionaryCursor.execute('''
            select * from dictionary where word == ?
            ''',(word,)).fetchall()
    return data

def search_history():
    data = dictionaryCursor.execute("""
                                    select word from dictionary
                                    """).fetchall()
    data = [x[0] for x in data]
    print("Recent searches")
    print("----------------")
    for x in data:
        print(x)
    return data

def Delete_history():
    dictionaryCursor.execute("""
                            delete from dictionary
                            """)
    dictionaryDatabase.commit()