try:
    val = 12/0 #Divided by 0 error
    num = float(input("Enter a num "))
    print(num)
except ZeroDivisionError:
    print("You cannot divide by zero moron")
except ValueError:
    print("Thats not a number you dumbfuck")
    # print("Invalid Input")