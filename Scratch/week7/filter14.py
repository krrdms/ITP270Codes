scores = [72, 68, 91, 100, 81]


def letterGrade(n):
    return 'A' if n >= 90 else 'B' if n >= 80 else 'C' if n >= 70 else 'D' if n >= 60 else 'F'


def passed(n):
    return True if n in ["A", "B", "C"] else False


grades = map(letterGrade, scores)

# note had to cover map object to list with cast
passGrades = filter(passed, list(grades))

print("grades:")
for grade in grades:
    print(grade)

print("show only passing grades:")
for pg in passGrades:
    print("passed:"+pg)
