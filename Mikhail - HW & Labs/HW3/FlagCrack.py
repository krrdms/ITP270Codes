# -------------- REQUIRED: add tqdm package to python interpreter in pycharm --------------- #
import zipfile
from itertools import permutations
import string


def flag():
    from tqdm import tqdm
    wordlist = "dictionary.txt"
    zf = str(input("\nEnter the name of the file you want to crack (Including the extension): "))
    # initialize the Zip File object
    zf = zipfile.ZipFile(zf)

    n_words = len(list(open(wordlist, "rb")))
    # print the total number of passwords
    print("\nTotal passwords to test:", n_words)

    with open(wordlist, "rb") as wordlist:
        for word in tqdm(wordlist, desc='Searching for password', total=n_words, unit="word"):
            try:
                zf.extractall(pwd=word.strip())
            except Exception:
                continue
            else:
                print("╔════════════════════════════╗\n [+] Password found:", word.decode().strip(),
                      '\n╚════════════════════════════╝')
                exit(0)
    print("[!] Password not found, try another wordlist. ㋡\n ")
    return word


def brute():
    import tqdm
    z1 = input("Enter the name of the file you want to crack (Including the extension): ")
    z = zipfile.ZipFile(z1)
    # chars = ['n',
    #          'y', 'z', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7',
    #          '8', '9']
    chars = ['P', 'b', 'c', 'P', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'a',
             'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # chars = string.ascii_letters + string.digits # Uncomment out to use the entire alphabet and digits
    iterator = tqdm.tqdm(permutations(chars, 4), desc='Cracking password', total=len(chars) ** 4, unit='pwd')
    # print(i)   #  Uncomment to see if it is working properly
    for i in iterator:
        i = "".join(i)
        password = i.encode()
        try:
            z.extractall(pwd=password.strip())
            iterator.close()
            print(f'╔════════════════════════════╗\n [+] Password found: {i}',
                  '\n╚════════════════════════════╝')
            exit(0)
        except Exception:
            pass


def main():
    while (True):
        print(f'''                  -|-
                   |
               .-'~~~`-.
             .'         `.
             |  R  I  P  |
             |           |
             |ᕈᗩᔕᔕᗯᗝᖇᖱᔕ|
           \\\|           |//     
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^''')
        print(
            '╔═════════════════════════════════════╗\n║1 ▶ Crack password using \033[1mdictionary\033[0m  ║ 📖 \n║2 '
            '▶ Crack password using \033[1mbrute force ║ \033[0m☠️\n║3 ▶ Quit                             ║ 🚫 '
            '\n╚═════════════════════════════════════╝\n')
        x = int(input('\nWhat would you like to do? '))
        if x == 1:
            flag()
        if x == 2:
            brute()
        if x == 3:
            print(f'''\n       _    (^)
      (_\   |_|
       \_\  |_|
       _\_\,/_|
      (`\(_|`\|
     (`\,)  \ \\
      \,)   | |      
        \__(__|''')
            break


main()
