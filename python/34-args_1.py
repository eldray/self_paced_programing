# *args = parameter that will pack all arguments into a tuple
# useful so that a function can accept a varying amount of arguments

#def add(num1, num2):
#    sum = num1 + num2
#    return sum

# this line prints an error
# print(add(1,2,3))

# we fix it by using *args
def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(add(1,2,3,4,5,6))
# args can be renamed to what ever name you want but must have the *