import random

scores = []
grades = []


def letterGrade(n):
    return 'A' if n >= 90 else 'B' if n >= 80 else 'C' if n >= 70 else 'D' if n >= 60 else 'F'


for idx in range(0, 24):
    scores.append(random.randrange(50, 90))


grades_ = map(letterGrade, scores)
for grade in grades_:
    grades.append(grade)

print(scores)
print(grades)
