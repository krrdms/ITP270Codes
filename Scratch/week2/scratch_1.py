#example code using Map and Filter

scores = [72, 88, 91, 100, 81]


def letter_grade(n):
    return 'A' if n >= 90 else 'B' if n >= 80 else 'C' if n >= 70 else 'D' if n >= 60 else 'F'


grades = map(letter_grade, scores)


def passed(n):
    return True if n in ["A", "B", "C"] else False


passing_grades = filter(passed, grades)

for grade in grades:
    print(grade)

for pg in passing_grades:
    print ("passed:"+pg)

