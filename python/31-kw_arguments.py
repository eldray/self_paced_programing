 #keyword arguments = arguments preceded by an identifier when we pas them to a function
 #               The order of the args doesnot matter unlike positional arguments

 #Eg of positional args
def hello(first, middle, last):
     print("Hello " + first + " " + middle + " " + last)

hello("James", "Kimani", "Spencer")

#converting to keyword args
def hello(first, middle, last):
     print("Hello " + first + " " + middle + " " + last)


hello(first="James", middle="Kimani", last="Spencer")
#works irrespective of the position
hello( middle="Kimani", first="James", last="Spencer")