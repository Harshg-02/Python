# Recursion is the process of defining something in term of it self


def factorial(n):
    if(n==0 or n==1):
     return 1
    else:
       return n*factorial(n-1)
    
print(factorial(3))
print(factorial(5))
print(factorial(7))