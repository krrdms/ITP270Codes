from zipfile import ZipFile
import itertools
import string
import zipfile

# control target with just 'password' & launcher function
# def testcontrol(curr_guess, zipedfile):
#     password = curr_guess
#     print("curr_guess=>", curr_guess, "<")
#     encoding = "utf-8"
#     zf = zipedfile
#
#     try:
#         with ZipFile(zf) as z:
#             z.extractall(pwd=bytes(password, encoding))
#             print("HEY WAIT I DECRYPTED")
#             with open("Flag.easy.zip", 'r') as p:
#                 data = p.readlines()
#                 print(data)
#                 print("yay I did it")
#                 return 1
#     except RuntimeError as e:
#         return -1
# testcontrol(curr_guess, zipedfile)
# dictionary password cracker
def dicpass():
    dictfile = 'dictionary.txt'
    tries=0

    for word in dictfile.readlines():
        word = word.strip('\n')
        word = word.rstrip()
        word = word.lstrip()
        tries+=1
        print("how many -", tries)
        #res = testcontrol(word, "Flag.dic.zip")
        res = testcontrol(word, "Flag.easy.zip")
        if res == 1:
            print("[+] !!!!!!!!! Found Password:", word)
            return
    print("[-] Password Not Found")
    return

# #  Brute force
# def crackpass(max_password_length):
#     zf = "Flag.brute.zip"
#     chars = 0
#     while chars < max_password_length:
#         chars += 1
#         for guess in itertools.product(
#                 string.digits + string.ascii_lowercase + string.ascii_uppercase + "!@#$%^&*+" + "",
#                 repeat=chars):
#             guess = ''.join(guess)
#             print("[-]Try:", guess)
#             password = guess
#             encoding = "utf-8"
#             try:
#                 with ZipFile(zf) as z:
#                     z.extractall(pwd=bytes(password, encoding))
#                     with open("Flag.txt") as p:
#                         data = p.readlines()
#                         print(data)
#                         print("very done")
#                         return 1
#             except RuntimeError as e:
#                 print(e.message)


# if __name__ == "__main__":
#     print("starting the control test first")
#     testcontrol('password', "Flag.easy.zip")
#     print("now doing the dictionary test on Flag.zip")
#     dicpass()
#     max_password_length = 8
#     print("now doing the brute test on Flag.zip")
#     zf = "Flag.brute.zip"
#
#     crackpass(max_password_length)
#