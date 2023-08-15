tup = (3, 5, 23, 52, 4, 24, 4)
print(type(tup), tup)
# tup[0]=6             #show error because tuple can not change

if 23 in tup:
    print("yes number is present")
else:
    print("number is not present")

tp = tup[1:4]  # creating new tuple which contain the value of existing couple
print(tp)
