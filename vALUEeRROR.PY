def getint(question, min, max):
    while True:
        try:
            a = int(input(question))
            if (a > min and min is not None):
                break
            elif (a > max and max is not None):
                pass
            else:
                return a
        except ValueError as e:
            print (f"{e}\nplease enter a whole number")
            continue

num1 = getint("Please enter a whole number", None, None)
num2 = getint("Please enter a whole number", None, None)
print (num1+num2)