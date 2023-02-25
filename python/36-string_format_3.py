# str.format() = a format method available to strings
# gives more control when displaying an output

name = "Evander"

print("Hello, my name is {}".format(name))
print("Hello, my name is {:15}, but I don't take liken to the famous boxer".format(name))
print("Hello, my name is {:<15}, but I can kick left".format(name)) #left align
print("Hello, my name is {:>15},  I can kick right".format(name)) #right align
print("Hello, my name is {:^15}, and  I can give you upper cut".format(name)) #center align
