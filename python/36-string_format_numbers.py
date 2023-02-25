# str.format() = a format method available to strings
# gives more control when displaying an output

pi_number = 3.14159
number = 1000

print("The number pi is {}".format(pi_number))
print("The number pi is {:.3f}".format(pi_number)) #rounding up float
print("The number is {}".format(number))
print("The number is {:,}".format(number))
print("The number is {:b}".format(number)) # convert to binary
print("The number is {:o}".format(number)) # convert to octane number
print("The number is {:X}".format(number)) # convert to hexadecimal
print("The number is {:E}".format(number)) #convert to scientific notation