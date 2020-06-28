try:
    num = float(input("Enter a num "))
    num2 = float(input("Enter another num "))
    nu3 = num / num2
    print(nu3)
except ValueError:
    print("Incorrect value")
except ZeroDivisionError as err:    #you can store the error as a variable :)
    print(err)
    print("Cannot divide by 0")