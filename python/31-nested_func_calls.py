# nested function calls = function calls inside another duction calls
#innermost unction call are resolvd first
#returned value is used as arument for the next outer function

#case scenario
num = input("Enter a whole positive number: ")
num = float(num)
num = abs(num)
num = round(num)
print(num)

# nested function case
print(round(abs(float(input("Enter a whole positive number: ")))))