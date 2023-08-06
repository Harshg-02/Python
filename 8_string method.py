# string are immutable
a = "Hello"
print(a.upper())  # to make character in upper case
print(a.lower())  # to make character in lower case

b = "Hello!!!!!!!"
print(a.rstrip("!"))  # this method remove trailing character


print(a.replace("Hello", "world"))  # replace 'hello' to 'world'

c = "this is python language"
print(c.capitalize())  # make first letter captial

c = "this is python language"
print(c.center(50))  # it will give 50 spaces from the starting

c = "this is python language"
print(c.endswith("e"))  # this give true if it is end with "e"

c = "this is python language"
print(c.find("is"))  # it give the index of "is"

c = "this is python language"
print(c.islower())  # check all  letter is in lower case or not

c = "this is python language"
print(c.isupper())  # check all  letter is in upper case or not

cc="this is python language\n"
print(c.isprintable()) #it not take \n because it is not a printable character

d = "hey world hey "
print(d.count("hey"))  # it will give the count of the given word

e="I am Good boy"
print(e.swapcase()) #it convert uppercase into lowercase and vice-versa