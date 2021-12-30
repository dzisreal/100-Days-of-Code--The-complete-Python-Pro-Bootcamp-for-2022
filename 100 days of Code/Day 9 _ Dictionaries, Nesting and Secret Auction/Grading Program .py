students_score = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

students_grade = {}

for i in students_score:
    score  = students_score[i]
    if score < 70:
        students_grade[i] = "Fail"
    elif 70 < score < 80:
        students_grade[i]  = "Acceptable"
    elif 80 < score < 90:
        students_grade[i] = "Exceeds Expectations"
    else:
        students_grade[i] = "Outstanding"

print(students_grade)

