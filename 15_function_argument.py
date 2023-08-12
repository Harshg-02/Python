# Default argument
# keyword argument
# variable length argument
# required argument


#default argument
def average(a=1,b=5):    # We pass the default value here
   print("average is", (a+b)/2)

average() 

def name(fname="ok" ,mname="fine"):
   print("name is" , fname,mname)

name("hello")

name(mname="noo")  #keyword argument we can change the value

def averagee(*numbers):    #it take  number as a tuple
   sum=0
   for i in numbers:
      sum=sum+i
   print("the average is" ,sum/len(numbers))

averagee(5,5,5)


# def averagee(**name):       it take name as a dictoniary

