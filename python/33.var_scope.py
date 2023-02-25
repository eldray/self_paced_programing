#scope = The region that a variable is recognized
#       A variable is only available from inside the region it is created
#       A local and a globally scoped version of a variab;e can be created

name = "Lincoln" 
# a global scope (available inside and outside the funtions) 
# but its within the current module we are working with.

def display_name():
    name = "Gates" # a  local scope (available only inside this function
    print(name)

display_name()
print(name)

# Python uses the L= Local E =Enclosing G=Gobal B =Built-in
