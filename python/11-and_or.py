 # logical operators (and, or, not)
 # used to check if conditions are related

temp = int(input("What is the temperature outside? "))

if temp >= 0 and temp <= 30:
     print("The weather is good today!")
     print("Go outside!")
elif temp < 0 or temp < 30:
    print("The weather is bad today!")
    print("Stay inside!")