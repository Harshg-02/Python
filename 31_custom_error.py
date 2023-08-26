a=int(input("enter the number"))
if(a<5 or a>9):
    raise ValueError("number should be greater than 5 and less than 9")