import re

def part1():
    pn = input('Enter a phone number: ')

    # inputs
    # (703)555-1212

    def isValid(pn):
        exp = "\([0-9]{3}\)[0-9]{3}-[0-9]{4}"
        res = re.findall(exp, pn)
        if len(res) == 0:
            return False
        return len(res[0]) == len(pn)

    print(isValid(pn))


def part2():
    pn = input("Enter a phone number: ")

    # inputs
    # 7035551212
    # (703)555-1212
    # 703-555-1212
    def isValid(pn):
        # all possible regex for numbers
        exps = ["\([0-9]{3}\)[0-9]{3}-[0-9]{4}", "[0-9]{10}", "[0-9]{3}-[0-9]{3}-[0-9]{4}"]
        # checking for each of the regex
        for exp in exps:
            res = re.findall(exp, pn)
            # if match is found
            if len(res) != 0 and len(res[0]) == len(pn):
                return True
        # if not a match
        return False

    print(isValid(pn))
    url = '<a href="https://www.google.com">'
    print("\n" + re.findall("https:.*[com]", url)[0])


def part3():
    def findValidPNs(pns):
        exps = ["\([0-9]{3}\)[0-9]{3}-[0-9]{4}", "[0-9]{10}", "[0-9]{3}-[0-9]{3}-[0-9]{4}"]
        res = []  # storing valid phone numbers (pn's)
        for exp in exps:
            res_temp = re.findall(exp, pns)
            res += res_temp  # appending the valid numbers
        print(res)

    pns = "(703)555-1212 293889203 (301)201-1011 3928392920 (571)321-4433 jdjd"
    findValidPNs(pns)

while True:
    print('\n1: Part 1\n2: Part 2\n3: Part 3\n')
    x = int(input("Enter the corresponding number: "))
    if x == 1:
        part1()
        continue
    if x == 2:
        part2()
        continue
    if x == 3:
        part3()
        continue
    else:
        break
