# learn about python lambda, map, filter and reduce

# VS Code rewrites lambda to def so I will comment the functions as they're originally written in lambda

# original lambda function:
# squared = lambda num: num * 2
from functools import reduce
def squared(num): return num * num


print(squared(4))

# original lambda function:
# addTwo = lambda num: num + 2


def addTwo(num): return num + 2


print(addTwo(14))

# sum = lambda a, b : a + b


def sum_total(a, b): return a + b


print(sum_total(5, 7))

#######################


def functionBuilder(x):
    # notice VS code leaves lambda the way it was inside a function
    return lambda num: num + x


addTen = functionBuilder(10)
addTwenty = functionBuilder(20)

print(addTen(7))
print(addTwenty(20))

###############################

numbers = [3, 7, 12, 18, 20, 21]

squared_nums = map(lambda num: num * num, numbers)

print(list(squared_nums))

##############################


odd_nums = filter(lambda num: num % 2 != 0, numbers)

print(list(odd_nums))

################################

# acc (short for accumulator) stores the running total.
# curr (short for current item) is the current name in the list.
# len(curr) gets the length (number of characters) in curr.
# acc + len(curr) adds that length to the running total.


lambda acc, curr: acc + curr

numbers = [1, 2, 6, 4, 5, 3]

total = reduce(lambda acc, curr: acc + curr, numbers, 10)

print(total)

print(sum(numbers, 10))


names = ['Sui generis', 'Ada Eze', 'Constance Chimdiya Ihekerem']

char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)

print(char_count)
