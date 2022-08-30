'''
Get every line that starts with the word from, then extract the third word
from that line
'''
try:
    file = open('mbox-short.txt')
except OSError:
    print("File has not been found", file)
    quit()


def getThirdLetter(file):
    for line in file:
        currentLine = line.split()
        if len(currentLine) == 0:
            continue
        if currentLine[0] == "From":
            print(currentLine[2])


getThirdLetter(file)
