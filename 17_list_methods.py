li = [1, 3, 4, 5,]
li.append(6)
print(li)  # add element in last

lis = [1, 23, 23, 21, 15, 13, 5, 32, 3, 4, 5,]
lis.sort()
print(lis)
lis.sort(reverse=True)  # in reverse order
print(lis)
print(lis.count(5))  # for count how many times a element come

l = [1, 3, 6, 8, 89]
l.insert(1, 22)  # insert element in particular index
print(l)

colors = ["blue", "green",]
rainbow = ["red", "purple"]
colors.extend(rainbow)  # add other list in last of previous list
print(colors)

lt = [2, 3, 4, 5]
ltt = [34, 4, 4, 4]
lo = lt+ltt     # we concatinate two list
print(lo)
