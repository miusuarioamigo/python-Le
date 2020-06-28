# if you leave as below and enter a string or any other value but a number you are gonna have an error 
# so you use try/ex to catch that error and insult the user (ok maybe not but you get the point)
# use this as a reference
# num = float(input("Enter a num "))
# print(num)

try:
    num = float(input("Enter a num "))
    print(num)
except:
    print("Thats not a number you dumbfuck")
    # print("Invalid Input")