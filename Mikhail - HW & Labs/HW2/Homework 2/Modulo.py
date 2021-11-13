# divisible by 2 and 5 for a given integer

def result():
    if x % 5 == 0:
        print("Divisible by 5")
    else:
        print("Number is not divisible by 5")
    if x % 2 == 0 and x % 5 == 0:
        print("Number is divisible by both 2 and 5")
    else:
        print("Number is not divisible by both 2 and 5")
    if x % 2 == 0 or x % 5 == 0:
        print("number is divisible by either 2 or 5")
    else:
        print("number is not divisible by either 2 or 5")


x = int(input("\033[1m\033[4mEnter an integer:\033[0m "))
result()
