import random


def lineFile():
    tfile = open("text.txt", "r")
    Lines = tfile.readlines()

    count = 0

    for line in Lines:
        count += 1
        print("\nLine {}: {}".format(count, line.strip()))
    tfile.close()
    return Lines


def entireFile():
    tfile = open("text.txt", "r")
    entire = tfile.readlines()
    print("\n" + str(entire))
    tfile.close()
    return entire


def randline():
    lines = open("text.txt").read().splitlines()
    myline = random.choice(lines)
    print("\n" + str(myline))
    return myline


def countfile():
    file = open("text.txt", "rt")
    data = file.read()
    words = data.split()
    print("\nNumber of words in text file: ", len(words))
    file.close()
    return len(words)


def wfile():
    my_list = ["An apple a day, keeps the doctor away", "Speak of the devil", "Once in a blue moon",
               "When pigs fly", "Let the cat out of the bag", "Kill two birds with one stone",
               "To add insult to injury",
               "Don't judge a book by its cover", "Break a leg", "Call it a day"]
    with open("Phrases.txt", "a+") as f:
        for element in my_list:
            f.write(element + "\n")
    f.close()
    print("\033[1mCheck this folder for the new txt file!\033[0m")


def main():
    while (True):
        print("\033[1m-~-()-~-()-~-()-~-()-~-()-~-()-~-MENU-~-()-~-()-~-()-~-()-~-()-~-()-~-")
        print(
            "\033[1m1 -> Read and output entire text file                                 |\n2 -> Read a file into a list "
            "object and print it out line by line.    |\n3 -> Read a file into a list object and print a random line "
            "out.      |\n4 -> Read a file in and count (and print) the number of words.        |"
            "\n5 -> Write a list to a file                                           |\n6 -> Quit                                      "
            "                       |\n-~-()-~-()-~-()-~-()-~-()-~-()-~-MENU-~-()-~-()-~-()-~-()-~-()-~-()-~-\033[0m")
        c = int(input("\033[1mEnter your choice:\033[0m "))

        if c == 1:
            entireFile()
        elif c == 2:
            lineFile()
        elif c == 3:
            randline()
        elif c == 4:
            countfile()
        elif c == 5:
            wfile()
        else:
            break


main()
