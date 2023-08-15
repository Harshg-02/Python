# tuples are immutable
# if you want to change the tuple then change into list then change the list and again covert it into tuple
countries=("india","United states","spain","italy")
temp=list(countries)
temp.append("russia")
temp.pop(2)
countries=tuple(temp)
print(countries)


#you can perform methods of list into tuple by changing tuple into list