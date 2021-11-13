def letterGrade(score):
    global letter
    if score >= 90:
        letter = '\033[1m-------\n' + str(x) + ' = \033[4mA\033[0m\n\033[1m-------\033[0m'
    elif score >= 80:
        letter = '\033[1m-------\n' + str(x) + ' = \033[4mB\033[0m\n\033[1m-------\033[0m'
    elif score >= 70:
        letter = '\033[1m-------\n' + str(x) + ' = \033[4mC\033[0m\n\033[1m-------\033[0m'
    elif score >= 60:
        letter = '\033[1m-------\n' + str(x) + ' = \033[4mD\033[0m\n\033[1m-------\033[0m'
    else:
        letter = '\033[1m-------\n' + str(x) + ' = \033[4mF\033[0m\n\033[1m-------\033[0m'
    return letter


x = int(input("Enter Grade Score: "))
print(letterGrade(x))
