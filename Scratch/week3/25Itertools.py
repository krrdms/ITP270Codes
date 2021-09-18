import itertools
import string

password = "g3T!"

for guess in itertools.product(string.digits+string.ascii_lowercase+string.ascii_uppercase+"!@#$%^&*+"+"",
                                   repeat=4):
    guess = ''.join(guess)
    print(guess)
    if guess == password:
        print(guess)
        break
