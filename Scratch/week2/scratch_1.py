scores = [72,88,91,100,81]

def lettergrade(n):
    return 'A' if n >= 90 else 'B' if n >= 80 else 'C' if n >= 70 else 'D' if n >= 60 else 'F'

grades = map(lettergrade, scores)

def passed(n):
    return True if n in ["A","B","C"] else False

passgrades =  filter(passed,grades)

for grade in grades:
    print (grade)

for pg in passgrades:
    print ("passed:"+pg)

