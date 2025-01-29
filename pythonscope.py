name = "Chimdiya"
count = 1


def beauty():
    color = "purple"
    global count
    count += 1
    print(count)

    def greeting(name):
        nonlocal color
        color = "red"
        print(color)
        print(name)

    greeting("Diya")


beauty()
