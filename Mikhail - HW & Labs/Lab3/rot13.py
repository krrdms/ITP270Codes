def encrypt(text):
    encrypted_text = ""
    for letter in text:
        if letter.isupper():
            encrypted_text += chr((ord(letter) + 13 - 65) % 26 + 65)
        elif letter.islower():
            encrypted_text += chr((ord(letter) + 13 - 97) % 26 + 97)
        else:
            encrypted_text += letter
    return encrypted_text


def decrypt(text):
    decrypted_text = ""
    for letter in text:
        if letter.isupper():
            decrypted_text += chr((ord(letter) - 13 - 65) % 26 + 65)
        elif letter.islower():
            decrypted_text += chr((ord(letter) - 13 - 97) % 26 + 97)
        else:
            decrypted_text += letter
    return decrypted_text


if __name__ == "__main__":
    while(True):
        print("\033[1m-()-MENU-()-")
        print("\033[1m1 -> Encrypt\n2 -> Decrypt\n3 -> Quit\033[0m")
        c = int(input("\033[1mEnter your choice:\033[0m "))

        if c == 1:
            text = input("\033[1mEnter message you want encrypted:\033[0m ")
            print("\033[1mEncrypted text:\033[0m ", encrypt(text))
        elif c == 2:
            text = input("\033[1mEnter message you want decrypted:\033[0m ")
            print("\033[1mDecrypted text:\033[0m ", decrypt(text))
        else:
            break
