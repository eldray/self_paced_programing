# *args = parameter that will pack all arguments into a tuple
# useful so that a function can accept a varying amount of arguments

def add(*stuff):
    sum = 0
    stuff = list(stuff) # changing tuple to a list to accep the argument
    for i in stuff:
        sum += i
    return sum

print(add(1,2,3,4,5,6))
# args can be renamed to what ever name you want but must have the *