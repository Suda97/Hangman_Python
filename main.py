import random
import os


def openFile():
    with open('words.txt', 'r') as f:
        line = f.readline().strip()
        file = []
        while line:
            line = f.readline().strip()
            file.append(line)
        f.close()
    file.pop()
    word = file[random.randint(0, len(file) - 1)]
    return word

def convert(string):
    list = []
    list[:0] = string
    return list

def gameLogic(word):
    wordl = convert(word)
    hidwor = []
    letters = []
    for _ in wordl:
        hidwor.append("_")
    print(hidwor)
    gamecounter = 0
    while True:
        userin = input("Guess Your letter: ")
        letters.append(userin)
        os.system('clear')
        userin = userin.capitalize()
        count = 0
        good = False
        for i in wordl:
            if wordl[count] == userin:
                hidwor[count] = userin
                good = True
            count += 1
        if good == False:
            gamecounter += 1
            print("Wrong!!")
        if gamecounter == 6:
            print("Word: " + word + "\nYou lose!!")
            break
        print("Tries: " + str(gamecounter) + "/6")
        print("Letters used:")
        print(letters)
        print(hidwor)
        ## print(wordl)
        win = True
        count = 0
        for i in hidwor:
            if hidwor[count] == "_":
                win = False
            count += 1
        if win:
            print("Word: " + word + "\nYou win!!")
            break


if __name__ == '__main__':
    gameLogic(openFile())
