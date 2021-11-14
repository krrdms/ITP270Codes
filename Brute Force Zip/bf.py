import zipfile
import itertools
import string


def openZipFile(filename,password):
    encoding = "utf-8"

    try:
        with zipfile.ZipFile(filename) as z:
            z.extractall(pwd=bytes(password, encoding))
            with open("Flag.txt") as p:
                data = p.readlines()
                print(data)
                return True
    except Exception as e:
        pass
    return False


def main():
    zf = "Flag.brute.zip"
    max_password_length = 4
    # global password
    chars = 3
    while chars < max_password_length:
        chars += 1
        for guess in itertools.product(
                string.ascii_uppercase + string.ascii_lowercase + string.digits + "!@#$%^&*+" + "",
                repeat=chars):
            guess = ''.join(guess)
            print("[-]Try:", guess)
            if openZipFile(zf, guess):
                print("[*]Hit:", guess)
                return


if __name__ == "__main__":
    # execute only if run as a script
    main()

