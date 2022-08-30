num = 0
total = 0
count = 0
average = 0
while True:
    try:
        num = int(input("Enter a number: "))
        if num == '':
            break
    except:
        print("Invalid input")
    count += 1
    average = (num + average) / count
    total += num
print(total, count, average)





