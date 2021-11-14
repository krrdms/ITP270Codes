import crypt
import time


def testPass(cryptPass):
    salt = cryptPass[0:2]
    dictFile = open('dictionary.txt')
    for word in dictFile.readlines():
        word = word.strip('\n')
        cryptWord = crypt.crypt(word, salt)
        if cryptWord == cryptPass:
            print("[+] Found Password:", word)
            return True
    print("[-] Password Not Found")
    return False


def main():
    startTime = time.time()
    passFile = open('passwords.txt')
    print("Password File loaded: %ds" % (time.time() - startTime))
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(":")[0]
            cryptPass = line.split(":")[1].strip(' ')
            print("[*] Cracking Password for: ", user)
            if testPass(cryptPass):
                print("Time Elapsed: %ds" % (time.time() - startTime))
    print("Exiting - Total Time: %ds" % (time.time() - startTime))


if __name__ == "__main__":
    main()
