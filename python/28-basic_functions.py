 # function = a block of code which is executed only when it is called

# function/block of code
def hello():
    print("hello ")
    print("Have a nice day!")

# invoking or calling the function
hello()
hello()

#adding arg to a ffunction
def hello(name):
    print("Hello " + name)
    print("Its wonderful you're taking this serious!")

hello("Emmanuel")


#adding more arguments
def hello(first_name,last_name, age):
    print("Hello " + first_name + " "  + last_name)
    print("You are now " + str(age)+ " years old")

hello("Dennis", "Churchill", 26)