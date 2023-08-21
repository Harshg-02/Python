s={1,2,5,6}
s2={3,6,7}
print(s.union(s2))  #for union
s.update(s2)
print(s ,s2)

s3={"delhi","mumbai","Gujrat","Banglore"}
s4={"Banglore","Delhi", "Gurugram","Noida"}
print(s3.intersection(s4))
s3.intersection_update(s4)   #for intersection


h={"ashis","harsh","akash","ankit"}
h1={"ashis","Rohan","ankit"}
# h1={"ashis","ankit"}  this is superset of original set

print(h,h1)
print(h.symmetric_difference(h1)) #for symmetric difference

print(h.isdisjoint(h1))  #disjoint set

print(h.issuperset(h1))  #super set(check all the item in particular set are present in original set)

print(h.issubset(h1))   # h1 is subset of h or not

h.add("Kolkata")  #add element in set
print(h)

h.remove("harsh")
print(h)

# (del) you can delete entire set by using this keyword
#(clear)  used to clear all the element of the set