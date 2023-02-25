# exception = event detected during the execution that interupts the normal flow of the program

#case scenario where input is 5/0 to print an error

try:
    numerator = int(input("Enter a numer to divide: "))
    denominator = int(input("Enter a numer to divide by: "))
    result = numerator / denominator

except ZeroDivisionError as e: #e is printing the error as it is
    print(e)
except ValueError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(result) # printing result as it is
finally:print("This will always execute") # last line to print  no matter the argument