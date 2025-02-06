# while loops and how they evaluate the true or false conditions

value = "y"
count = 0

while value:
    count += 1
    print(count)
    if (count == 5):
        break
    else:
        value = 0
        continue
