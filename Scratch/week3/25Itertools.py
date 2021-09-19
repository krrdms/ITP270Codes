import itertools
import string

password = "g3T!"
max_password_length = 8

def crackPass(max_password_length):
    # global password
    chars = 0
    while chars < max_password_length:
        chars += 1
        for guess in itertools.product(
                string.digits + string.ascii_lowercase + string.ascii_uppercase + "!@#$%^&*+" + "",
                repeat=chars):
            guess = ''.join(guess)
            print("[-]Try:", guess)
            if guess == password:
                print("[*]Hit:", guess)
                return


crackPass(max_password_length)


if __name__ == "__main__":
    crackPass(max_password_length)
