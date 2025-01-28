name = "Chimdiya"
count = 1


def beauty():
    color = "purple"
    global count
    count += 1
    print(count)


# global performs the same function as non local


    def greeting(name):
        nonlocal color
        color = "red"
        print(color)
        print(name)

    greeting("Diya")


beauty()
