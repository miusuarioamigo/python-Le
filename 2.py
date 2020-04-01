def divstr(string):
    li = list(string.split(" "))
    return li

a = input("write something here: ")
b = divstr(a)

print(b[2])

for i in b:
    print(i)