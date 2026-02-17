try:
    num1, num2 = eval(input("Please enter 2 numbers seperated by a comma"))
except (ZeroDivisionError, SyntaxError, BaseException):
    print ("you failure")
finally:
    print ("your still a failure") #Dare