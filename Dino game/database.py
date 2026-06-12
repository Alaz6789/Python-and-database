import sqlite3

dinoDatabase = sqlite3.connect('Dino database.db')
dino_cursor = dinoDatabase.cursor()
dino_cursor.execute("""create table if not exists users(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE,
                    passwod TEXT
                    )""")

dino_cursor.execute("""create table if not exists scores(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT,
                    score INTEGER
                    )""")

def sign_up(username, password):
    validstatus = dino_cursor.execute('''
                select * from users where username == ?
                ''',(username,))
    if validstatus.fetchone():
        print("This username is already taken. Please choose a different username.")
        return
    else:
        dino_cursor.execute('''
                insert into users(username, password) values(?,?)
                ''',(username,password))
        print("Account created successfully!")
        dinoDatabase.commit()

def sign_in(username, password):
    validstatus = dino_cursor.execute('''
                select * from users where username == ? and password == ?
                ''',(username, password))
    if validstatus.fetchone():
        print("You have signed in!")
    else:
        print("This account is not regsitered")

def update_password(username):
     account = dino_cursor.execute('''
                select * from users where username == ?
                '''(username,))
     if account.fetchall():
        new_password = input("What is the new password: ")
        dino_cursor.execute('''
        update users
        set password = ?
        from users where username == ?
        ''',(new_password, username))

def delete_account(username):
     account = dino_cursor.execute('''
                select * from users where username == ?
                '''(username,))
     if account.fetchall():
        dino_cursor.execute('''
        delete from users where username == ?
        ''',(username,))
     account = dino_cursor.execute('''
                select * from scores where username == ?
                '''(username,))
     if account.fetchall():
        dino_cursor.execute('''
        delete from scores where username == ?
        ''',(username,))

def save_score(username, score):
    dino_cursor.execute('''
                insert into scores(username, score) values(?,?)
                '''(username, score))
    print("Your score was successfully saved")
    dinoDatabase.commit()

def get_high_score(username):
    dino_cursor.execute('''
                select username, max(score) from scores where username == ?
                '''(username,))
    data = dino_cursor.fetchall()
    for item in data:
                 print(f"""
                       -----------------
                       name : {item[0]}
                       score : {item[1]}
                       ------------------
                       """)
                 

dinoDatabase.close()