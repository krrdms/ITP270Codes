import random
import string
# import re I was trying to remove certain special characters from string.punctuation, but wasn't sure how to without
# just placing the special characters that I wanted only in the password :(


def num3():
    num = 0
    for i in range(0, 100):
        num = num + 1
        if num % 2 == 0 and num % 7 == 0:
            print(num)
            continue
        else:
            pass


def password():

    class PasswordGenerator:
        pw_len = 8

        upper = string.ascii_uppercase
        lower = string.ascii_lowercase
        digits = string.digits
        specials = string.punctuation

        allchars = upper + lower + digits + specials

        def generate(self):
            password = random.choice(self.upper)
            password += random.choice(self.lower)
            password += random.choice(self.digits)
            password += random.choice(self.specials)

            password += ''.join(random.sample(self.allchars, self.pw_len - 4))

            password = ''.join(random.sample(password, len(password)))
            return password

    pw_generate = PasswordGenerator()
    print(pw_generate.generate())

while True:
    print('\n1 -> Show output for number 3\n2 -> Show output for number 4')
    x = int(input('\nPlease choose an option: '))
    if x == 1:
        num3()
    if x == 2:
        password()
    else:
        break
