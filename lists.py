users = ['Chimdiya', 'Constance', 'Walter']

data = ['Chimdiya', '20', 'True']

emptylist = []

print("Chimdiya" in users)

print("Chimdiya" in emptylist)

print(users[0])
print(users[-2])

print(users.index('Walter'))

print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(len(data))

users.append('Kizito')
print(users)

users += ['Ada']
print(users)

users.extend(['Odogwu', 'Nnaemeka'])
print(users)

# users.extend(data)
# print(users)

users.insert(0, 'Stacie')
print(users)

users[2:2] = ['Iheke', 'Chinyere']
print(users)

users[1:3] = ['Obi', 'Adesewa']
print(users)

users.remove('Odogwu')
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

# del data
data.clear()
print(data)

users[1:2] = ['chimdiya']
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [4, 46, 58, 49, 73, 13, 90]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)


print(sorted(nums, reverse=True))
print(nums)

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))

mylist = list([1, "Chimdiya", True])
print(mylist)

# Tuples

mytuple = tuple(('Chimdiya', 20, True))

anothertuple = (1, 4, 3, 7, 3, 3, 3)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append('Constance')
newtuple = (newlist)
print(newtuple)

(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.count(3))
