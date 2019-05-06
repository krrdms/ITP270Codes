import crypt

def testPass(cryptPass):
    salt = cryptPass[0:2]
    dictfile = open('dictionary.txt')
    for word in dictfile.readlines():
        word = word.strip('\n')
        cryptWord = crypt.crypt(word, salt)
        if (cryptWord == cryptPass):
            print("[+] Found Password:", word)
            return
    print("[-] Password Not Found")
    return

def main():
    passFile = open('passwords.txt')
    for line in passFile.readlines():
        if ":"in line:
            user = line.split(":")[0]
            cryptPass = line.split(":")[1].strip(' ')
            print("[*] Cracking Password for: ", user)
            testPass(cryptPass)

if __name__ == "__main__":
    main()