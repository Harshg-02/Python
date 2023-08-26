# try:
#     l=[23,4,2,4]
#     i =int(input("enter the index number"))
#     print(l[i])
# except:
#     print("some error occured")

# finally:
#     print("i am always executed")


def fun1():
    try:
     l=[23,4,2,4]
     i =int(input("enter the index number"))
     print(l[i])
     return 1
    except:
     print("some error occured")
     return 0

    finally:
        print("i am always executed")

x=fun1()
print(x)



