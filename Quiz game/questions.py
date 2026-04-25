python_questions = [
{
"question": "Which keyword is used to define a function in Python?",
"options": ["A. function", "B. define", "C. def", "D. func"],
"answer": "C"
},
{
"question": "Which data type stores True or False?",
"options": ["A. int", "B. bool", "C. str", "D. float"],
"answer": "B"
},
{
"question": "What will print(len('Hello')) output?",
"options": ["A. 4", "B. 5", "C. 6", "D. Error"],
"answer": "B"
},
{
"question": "Which symbol is used for comments in Python?",
"options": ["A. //", "B. #", "C. /* */", "D. --"],
"answer": "B"
},
{
"question": "Which function takes input from user?",
"options": ["A. scan()", "B. read()", "C. input()", "D. get()"],
"answer": "C"
},
{
"question": "Which data structure stores multiple values?",
"options": ["A. list", "B. int", "C. float", "D. bool"],
"answer": "A"
},
{
"question": "What is the index of first element in Python list?",
"options": ["A. 0", "B. 1", "C. -1", "D. 2"],
"answer": "A"
},
{
"question": "Which loop runs while a condition is true?",
"options": ["A. for", "B. while", "C. loop", "D. repeat"],
"answer": "B"
},
{
"question": "Which keyword stops a loop?",
"options": ["A. stop", "B. break", "C. exit", "D. halt"],
"answer": "B"
},
{
"question": "Which library is used for databases like SQLite?",
"options": ["A. pandas", "B. sqlite3", "C. numpy", "D. turtle"],
"answer": "B"
}
]

sql_questions = [
{
"question": "Which SQL command is used to retrieve data?",
"options": ["A. INSERT", "B. UPDATE", "C. SELECT", "D. DELETE"],
"answer": "C"
},
{
"question": "Which command adds new data to a table?",
"options": ["A. INSERT", "B. SELECT", "C. CREATE", "D. UPDATE"],
"answer": "A"
},
{
"question": "Which SQL command deletes data?",
"options": ["A. REMOVE", "B. DELETE", "C. ERASE", "D. DROP"],
"answer": "B"
},
{
"question": "Which command creates a new table?",
"options": ["A. BUILD", "B. MAKE", "C. CREATE TABLE", "D. ADD"],
"answer": "C"
},
{
"question": "Which keyword filters rows?",
"options": ["A. WHERE", "B. FILTER", "C. LIMIT", "D. ORDER"],
"answer": "A"
},
{
"question": "Which command updates existing data?",
"options": ["A. CHANGE", "B. MODIFY", "C. UPDATE", "D. ALTER"],
"answer": "C"
},
{
"question": "Which SQL keyword sorts results?",
"options": ["A. SORT", "B. ORDER BY", "C. GROUP", "D. FILTER"],
"answer": "B"
},
{
"question": "Which function counts rows?",
"options": ["A. SUM()", "B. COUNT()", "C. TOTAL()", "D. ADD()"],
"answer": "B"
},
{
"question": "Which clause groups rows?",
"options": ["A. ORDER BY", "B. GROUP BY", "C. FILTER BY", "D. SORT"],
"answer": "B"
},
{
"question": "Which keyword limits number of rows returned?",
"options": ["A. LIMIT", "B. TOP", "C. MAX", "D. RANGE"],
"answer": "A"
}
]

sorting_questions = [
{
"question": "Which algorithm repeatedly swaps adjacent elements?",
"options": ["A. Bubble Sort", "B. Merge Sort", "C. Quick Sort", "D. Heap Sort"],
"answer": "A"
},
{
"question": "Which sorting algorithm uses divide and conquer?",
"options": ["A. Bubble Sort", "B. Merge Sort", "C. Selection Sort", "D. Insertion Sort"],
"answer": "B"
},
{
"question": "Which sorting algorithm picks smallest element each time?",
"options": ["A. Selection Sort", "B. Bubble Sort", "C. Quick Sort", "D. Heap Sort"],
"answer": "A"
},
{
"question": "Which sorting algorithm inserts elements into correct position?",
"options": ["A. Insertion Sort", "B. Bubble Sort", "C. Merge Sort", "D. Heap Sort"],
"answer": "A"
},
{
"question": "Which sorting algorithm uses pivot element?",
"options": ["A. Quick Sort", "B. Merge Sort", "C. Selection Sort", "D. Bubble Sort"],
"answer": "A"
},
{
"question": "Worst case time complexity of Bubble Sort?",
"options": ["A. O(n)", "B. O(n log n)", "C. O(n^2)", "D. O(log n)"],
"answer": "C"
},
{
"question": "Which sorting algorithm is fastest on average?",
"options": ["A. Bubble Sort", "B. Quick Sort", "C. Selection Sort", "D. Insertion Sort"],
"answer": "B"
},
{
"question": "Merge Sort time complexity?",
"options": ["A. O(n)", "B. O(n log n)", "C. O(n^2)", "D. O(log n)"],
"answer": "B"
},
{
"question": "Which algorithm is stable?",
"options": ["A. Bubble Sort", "B. Quick Sort", "C. Heap Sort", "D. None"],
"answer": "A"
},
{
"question": "Which sorting algorithm is simplest to understand?",
"options": ["A. Bubble Sort", "B. Heap Sort", "C. Quick Sort", "D. Merge Sort"],
"answer": "A"
}
]

import random

# Combine all lists into one
all_questions = python_questions + sql_questions + sorting_questions

# Randomly select 5 from the entire pool
selected_questions = random.sample(all_questions, 5)

for q in selected_questions:
    print(q["question"])