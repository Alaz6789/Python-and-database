import sqlite3

libraryDatabase = sqlite3.connect("Library Database.db")
library_cursor = libraryDatabase.cursor()
library_cursor.execute("""create table if not exists library(
    bookId INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    price INTEGER,
    status TEXT
    )""")

def add_book():
    title = input("What is the name of the book: ")
    author = input("Who wrote the book: ")
    price = int(input("What is the price: "))
    availability = "available"

    library_cursor.execute('''
                insert into library(title,author,price,status) values(?,?,?,?)
                ''',(title,author, price, availability))
    print("Book data added successfully!")
    libraryDatabase.commit()

def delete_book():
    id = input("What is the ID of the book you want to delete: ")
    find_book = library_cursor.execute('''
                select * from library where bookId == ?
                ''',(id,))
    if find_book.fetchall():
        library_cursor.execute('''
        delete from library where bookId == ?
        ''',(id,))
    else:
        print(f"There is no book with ID {id} in the database")
    libraryDatabase.commit()

def update_book():
    id = input("What is the ID of the book you want to update: ")
    find_book = library_cursor.execute('''
                select * from library where bookId == ?
                ''',(id,))
    if find_book.fetchall():
        title = input("What is the name of the book: ")
        author = input("Who wrote the book: ")
        price = int(input("What is the price: "))
        availability = "available"

        library_cursor.execute('''
            update library
            set title = ?, author = ?, price = ?, status = ?
            where bookId == ?
            ''',(title, author, price, availability, id))
        print("Book updated successfully!")
    else:
        print(f"There is no book with ID {id} in the database")
    libraryDatabase.commit()

def display_books():
    library_cursor.execute('''select * from library''')
    data = library_cursor.fetchall()

    for item in data:
        print(f"""
               ------------------
               ID : {item[0]}
               Title : {item[1]}
               Author : {item[2]}
               Price : {item[3]}
               Status : {item[4]}
               ------------------
                       """)

def status():
    id = input("What is the ID of the book you want to update: ")
    find_book = library_cursor.execute('''
                select status from library where bookId == ?
                ''',(id,))
    
    print(str(find_book))
    if find_book == "available":
        library_cursor.execute('''
                            update library
                            set status = "issued"
                            where bookId == ?
                            ''',(id,))
        print("Availability of the book: issued")
    elif find_book == "issued":
        library_cursor.execute('''
                            update library
                            set status = "available"
                            where bookId == ?
                            ''',(id,))
        print("Availability of the book: available")
    libraryDatabase.commit()


runningStatus = True

while runningStatus:
    choice = int(input("""
            =========================
            1. Add Book
            2. Delete Book
            3. Update Book
            4. Display Books
            5. Issue/Return Book
            6. Exit
            =========================
            """))
    if choice == 1:
        add_book()

    elif choice == 2:
        delete_book()

    elif choice == 3:
        update_book()

    elif choice == 4:
        display_books()

    elif choice == 5:
        status()

    elif choice == 6:
        print("You have exitted, Come back soon!")
        runningStatus = False

    else:
        print("Invalid option")

libraryDatabase.close()