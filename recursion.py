# recursive function

def add_one(num):

    if (num >= 9):
        return num + 1

    total = num + 1
    print(total)

    return add_one(total)


mynewtotal = add_one(0)
print(mynewtotal)


# using function definition and for loop to print 1 to 10

def num(a):
    for i in range(a, 11):  # Start from 'a' and go up to 10 (inclusive)
        print(i)


num(1)
