import re
import requests


def getNumbers():
    numberList = []

    data = requests.get("https://business.gmu.edu/undergraduate/current-students/contact-us/")
    content = data.content.decode()
    # print(content)
    phoneNumber = list(set(re.findall("[0-9]{3}-[0-9]{3}-[0-9]{4}", content)))
    return phoneNumber


def main():
    numbers = getNumbers()
    for number in numbers:
        print("found: ", str(number))


if __name__ == '__main__':
    main()
