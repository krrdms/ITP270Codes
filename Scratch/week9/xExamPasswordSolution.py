import string
import random

password = ""

for x in range(3):
    password += random.choice(string.ascii_lowercase)
for x in range(2):
    password += random.choice(string.ascii_uppercase)
for x in range(2):
    password += random.choice("!@#%*")
for x in range(1):
    password += random.choice(string.digits)
password = "".join(random.sample(password,len(password)))
print(password)