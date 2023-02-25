#**kwargs = prameter that will pack all arguments into a dictionary
# useful so that a function can accept a varying amount od keyword arguments

# kwargs can be replaced with any name but must have **
def hello(**names):
    print("Hello", end = " ")
    for key,value in names.items():
        print(value, end=" ")

hello(title="Dr.",first="Emmanuel",middle="Kusi",last="Appiah")