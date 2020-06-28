#Functions are a collection of instructions
# a collection of code

def function1():
    print("ahhhh")

print ("this is ouside the function")

function1()

#a mapping

def function2(x):
    return 2*x

a = function2(6)

print(a)

def plus(x,y):
    return x +y

b = plus(80, 20)
print(b)

def functionpe(x):
    print(x)
    print("still in this function")
    return 3*x

f = functionpe(4)
print(f)

def function5(some_argument):
    print(some_argument)
    print("weee")

function5("Lalala")
