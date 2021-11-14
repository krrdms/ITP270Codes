import itertools
import zipfile
import string
import time


def zipEasyCrack():
    zf = "Flag.easy.zip"
    password = "password"
    if openEncryptedZipFile(password, zf):
        print("success")
        return True
    return False


def zipDictCrack():
    startTime = time.time()
    zf = "Flag.zip"
    dictionary_file = "dictionary.txt"

    with open(dictionary_file) as df:
        guesses = 0
        for guess in df.readlines():
            guess = guess.rstrip()
            guesses += 1
            if guesses % 100000 == 0:
                print("Tried ", guesses, " guesses")
            if openEncryptedZipFile(guess, zf):
                print("hit:", guess)
                print("Elapsed: %s" % (time.time() - startTime))
                return True
    print("Elapsed: %s" % (time.time() - startTime))
    return False


def zipBruteCrack():
    startTime = time.time()
    zf = "Flag.brute.zip"
    chars = 4
    max_chars = 8

    while chars < max_chars:
        print("Trying %d characters..." % chars)
        for guess in itertools.product(
                string.ascii_uppercase + string.ascii_lowercase +  string.digits + "!@#$%^&*+" + "",
                repeat=chars):
            guess_ = ''.join(guess)
            if openEncryptedZipFile(guess_, zf):
                print("hit:", guess_)
                print("Elapsed: %s" % (time.time() - startTime))
                return True
            chars += 1
    print("Elapsed: %s" % (time.time() - startTime))
    return False


def openEncryptedZipFile(guess, zipFile):
    encoding = "utf-8"
    outputFile = "Flag.txt"
    try:
        print("guess: %s" % guess)
        with zipfile.ZipFile(zipFile) as z:
            z.extractall(pwd=bytes(guess, encoding))
            with open(outputFile) as p:
                data = p.readlines()
                if len(data) > 0:
                    print(data)
                    return True
    except Exception as e:
        pass

    return False


def main():
    #zipEasyCrack()
    zipDictCrack()
    #zipBruteCrack()


if __name__ == "__main__":
    # execute only if run as a script
    main()
