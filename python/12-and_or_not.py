# logical operators (not)
# used to check if two or more conditions is true

temp = int(input("What is the temperature outside? "))

if not(temp >= 0 and temp <= 30):
     print("The weather is good today!")
     print("Go outside!")
elif not(temp < 0 or temp < 30):
    print("The weather is bad today!")
    print("Stay inside!")