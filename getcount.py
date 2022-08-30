'''
Count the words in file using key value pairs
'''

try:
    file = open('intro.txt')
except EOFError:
    print('Cannot not find the file')
counts = dict()
for line in file:
    lines = line.rstrip()
    lines = line.upper().split()

    for words in lines:
        counts[words] = counts.get(words, 0) + 1

largestNum = -1
largestWord = ""

for key, value in counts.items():
    if value > largestNum:
        largestNum = value
        largestWord = key

print(largestWord, largestNum)



