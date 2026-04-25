import sqlite3
import questions
import random

quizDatabase = sqlite3.connect('Quiz Database.db')
quiz_cursor = quizDatabase.cursor() 
quiz_cursor.execute("""create table if not exists quiz(
    id INTEGER PRIMARY KEY,
    email TEXT,
    name TEXT,
    password TEXT,
    score INTEGER DEFAULT 0
    )""")

def createAccount():
    id = int(input("Enter a unique id: "))
    email = input("Enter your email: ")
    name = input("enter your name: ")
    password = input("Enter your password: ")

    validstatus = quiz_cursor.execute('''
               select * from quiz where id == ?
               ''',(id,))
    if validstatus.fetchone():
        print("This id is already taken. Please choose a different id.")
        return
    else:
        quiz_cursor.execute('''
                insert into quiz(id,email,name,password) values(?,?,?,?)
                ''',(id,email,name,password))
        print("Account created successfully!")
        quizDatabase.commit()

def signIn():
    id_answer = int(input("Enter your unique id: "))
    password = input("Enter your password: ")
    db_answer = quiz_cursor.execute('''
               select * from quiz where id == ? and password == ?
               ''',(id_answer,password,))
    if db_answer.fetchone():
        print("Sign in successful!")
    else:
        print("Invalid id or password. Please try again.")

def playquiz():
     id = int(input("Enter your unique id: "))
     current_score = quiz_cursor.execute('''
                                         select score from quiz where id == ? 
                                         ''',(id,))
     total = 0
     all_questions = questions.python_questions + questions.sql_questions + questions.sorting_questions
     selected_questions = random.sample(all_questions, 5)

     for q in selected_questions:
        print(q["question"])
        print(q["options"])
        answer = input("What is your answer?")
        if answer.upper() == q["answer"]:
            print("Correct!")
            total += 1
        else:
            print(f"Wrong! The correct answer is {q['answer']}.")
     if total > current_score:
        print(f"Your total score is: {total}")
        quiz_cursor.execute('''
                        update quiz set score = ? where id == ?
                        ''',(total,id,))

def myscore():
    id = int(input("Enter id: "))
    quiz_cursor.execute('''
               select name, score from quiz where id == ?
               ''',(id,))
    info = quiz_cursor.fetchone()
    print(f"""
           -----------------
        name : {info[0]}
        score : {info[1]}
           ------------------
        """)

def displayData():
        quiz_cursor.execute('''select * from quiz''')
        data = quiz_cursor.fetchall()
        
        for item in data:
                 print(f"""
                       -----------------
                       name : {item[2]}
                       score : {item[4]}
                       ------------------
                       """)
                 
def maxscore():
    quiz_cursor.execute('''
                    select name, score from quiz where score == (select max(score) from quiz)
                    ''')
    info = quiz_cursor.fetchone()
    print(info)

def top2():
     quiz_cursor.execute(f'''
                    select * from quiz order by score desc limit 2
                    ''')
     info = quiz_cursor.fetchall()
     print(info)
                 
runningstatus = True
runningstatus2 = True

while runningstatus:
        print("""
            =========================
            1. Create account
            2. Sign in
            3. Exit
            =========================
            """)
        option = int(input("Enter your choice : "))
        if option == 1:
            createAccount()
        elif option == 2:
            signIn()

            while runningstatus2:
                print("""
                    =========================
                    1. Play quiz
                    2. Show my score
                    3. Show all scores
                    4. Show maximum score
                    5. Show top 2 scorers
                    6. Logout
                    =========================
                    """)
                option2 = int(input("Enter your choice : "))
                if option2 == 1:
                     playquiz()
                elif option2 == 2:
                    myscore()
                elif option2 == 3:
                    displayData()
                elif option2 == 4:
                    maxscore()
                elif option2 == 5:
                    top2()
                elif option2 == 6:
                    runningstatus2 = False
                else:
                    print("Invalid option. Please try again.")

                quizDatabase.commit()

        elif option == 3:
            print("Thank you for playing!")
            runningstatus = False
        else:
            print("Invalid option. Please try again.")

quizDatabase.close()