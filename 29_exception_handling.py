# a=int(input("enter a number"))
# print(f"multiplication table of {a}is:")

# for i in range(1,11):
#     print(f"{int(a)}x{i}={int(a)*i}")

#some line of code that we want to execute after the error

#Exception handling
a=(input("enter a number"))
print(f"multiplication table of {a}is:")

try:
    for i in range(1,11):
     print(f"{int(a)}x{i}={int(a)*i}")
except Exception as e:
   print(e)

print("other line of code")



#syntax
# try:
#     some code
# except:
#   some code


try:
   num=int(input("enter a intager:"))
   a=[6,3]
   print(a[num])

except ValueError:
   print("number is not inteager")

except IndexError:
   print("Index error")