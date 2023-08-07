a=int(input("enter the age:"))
print("your age is ",a)

if(a>18):
    print("you can drive")
else:
    print("you can not drive")


# elif statement
num=int(input("enter the number"))
if(num>0):
    print("number is greater")
elif(num==0):
    print("number is equal to zero")
else:
    print("number is lesser")


# nested if else
num = 18
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")