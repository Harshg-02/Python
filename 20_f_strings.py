#it is used for string formatting
letter="my name is {} and i am from {}"
country="india"
name="hello"
print(letter.format(name,country))  #this is basic string formatting

print(f"my name is {name} and i am from {country}")
#this is f-string method you can directly put the value


price=49.0293
msg=f"the price is {price:.2f}"  # (.2f) take only two value after the decimal
print(msg)

print(f"{2*40}")   # another example


print(f"my name is {{name}} and i am from {{country}}")  # if you want to print f-string as it is