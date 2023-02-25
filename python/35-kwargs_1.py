#**kwargs = prameter that will pack all arguments into a dictionary
# useful so that a function can accept a varying amount od keyword arguments

#case scenario
# def hello(first, last):
#    print("Hello " + first + " " + last)
# prints an error because midle name is not specified
# hello(first="Emmanuel",middle="Kusi" last="Appiah+")

def hello(**kwargs):
    print ("Hello " + kwargs['first'] + " " + kwargs['last'] )

hello(first="Emmanuel",middle="Kusi",last="Appiah")