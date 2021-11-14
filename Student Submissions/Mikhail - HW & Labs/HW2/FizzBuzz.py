def fizzBuzz():
    num = 0
    for i in range(100):
        num = num + 1
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
            continue
        elif num % 3 == 0:
            print("Fizz")
            continue
        elif num % 5 == 0:
            print("Buzz")
            continue
        else:
            print(num)


if __name__ == "__main__":
    fizzBuzz()
