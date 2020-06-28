a = [3, 10, -1]

print(a)

a.append(5)

print(a)

#You can combine list w numbers and strings ex..

a.append("Hey")

print(a)

#a list can also contain other lists, ex..

a.append([1,2])
print(a)

#delete an item
a.pop()
print(a)

a.pop()
print(a)

#retrieve an specific space on the list
print(a[0])
print(a[3])

#changa a item on the list value
a[0] = 50
print(a)
