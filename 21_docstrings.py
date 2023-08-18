#python docstrings are the string literals that appear right after the defintion of function,methods,class or module

def square(n):
    '''take in the number n and returns the square of n'''
    print(n**2)
square(5)
print(square.__doc__)