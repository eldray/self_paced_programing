# exception = event detected during the execution that interupts the normal flow of the program

#case scenario where input is 5/0 to print an error

try:
    numerator = int(input("Enter a numer to divide: "))
    denominator = int(input("Enter a numer to divide by: "))
    result = numerator / denominator
    print(result)
except Exception:
    print("Something went wrong")