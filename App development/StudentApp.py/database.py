import sqlite3
from tkinter import *
import settings as s

StudentDatabase = sqlite3.connect('Student database.db')
student_cursor = StudentDatabase.cursor()
student_cursor.execute("""create table if not exists students(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT UNIQUE,
                    age INTEGER,
                    course Text
                    )""")

def add_student(name, age, course):
    validstatus = student_cursor.execute('''
                select * from students where name == ?
                ''',(name,))
    if validstatus.fetchone():
        print("This name is already taken. Please choose a different name.")
        return
    else:
        student_cursor.execute('''
                insert into students(name, age, course) values(?,?,?)
                ''',(name,age,course))
        print("Account created successfully!")
        StudentDatabase.commit()
    s.InputSpace.config(text = "Account created successfully!")

def display_students():
    student_cursor.execute('''
        select * from students
        ''')
    data = student_cursor.fetchall()
    s.InputSpace2.config(text = data)
    

def delete_student(name):
     student = student_cursor.execute('''
                select * from students where name == ?
                ''',(name,))
     if student.fetchall():
        student_cursor.execute('''
        delete from students where name == ?
        ''',(name,))
        print("Student was deleted successfully")
        StudentDatabase.commit()
        s.InputSpace3.config(text = "Student was deleted from the database")
     else:
         print("Student doesn't exist in the database")