value = 1

while value <= 10:
    print(value)
    if value == 5:
        break
    value += 1

# Bad way to use continue

# value = 1
# while value <= 10:
#     print(value)
#     if value == 5:
#         continue
#     value += 1

# right way to use continue plus else

while value <= 10:
    value += 1
    if value == 5:
        continue
    print(value)
else:
    print("value is now equal to " + str(value))

# Basic for loop

names = ["Chimdiya", "Nnaemeka", "Constance"]
for diya in names:
    print(diya)

for diya in "Iheke":
    print(diya)

# for loop with a break

for diya in names:
    if diya == "Nnaemeka":
        break
    print(diya)

# for loop with continue

for diya in names:
    if diya == "Nnaemeka":
        continue
    print(diya)

for diya in range(4):
    print(diya)

for diya in range(2, 4):
    print(diya)

for diya in range(0, 101, 5):
    print(diya)
else:
    print("Glad that\'s over!")

# Nested loops

names = ["Chimdiya", "Diya", "Constance"]
actions = ["codes", "reads", "sleeps", "eats"]

for name in names:
    for action in actions:
        print(name + " ", action + ".")

for action in actions:
    for name in names:
        print(name + " ", action + ".")
