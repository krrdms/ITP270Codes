import random

scores = []
grades = []


def letterGrade(n):
    return 'A' if n >= 90 else 'B' if n >= 80 else 'C' if n >= 70 else 'D' if n >= 60 else 'F'


def passed(n):
    return True if n in ["A", "B", "C"] else False


for idx in range(0, 3):
    scores.append(random.randrange(50, 90))


grades_ = map(letterGrade, scores)
for grade in grades_:
    grades.append(grade)

print(scores)
print(grades)

passGrades = filter(passed, list(grades))
print("show only passing grades:")
for pg in passGrades:
    print("passed:"+pg)