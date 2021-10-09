scores = [72, 68, 91, 100, 81]


def letterGrade(n):
    return 'A' if n >= 90 else 'B' if n >= 80 else 'C' if n >= 70 else 'D' if n >= 60 else 'F'


grades = map(letterGrade, scores)

for grade in grades:
    print(grade)
