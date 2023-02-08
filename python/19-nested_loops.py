#nested loops = the inner loop will finish all of its iterattions before finist the outer loops iteration
#this program prints a rectangular shape

rows = int(input("how many rows? "))
columns = int(input("How many columns? "))
symbol = input("Enter a symbol to use? ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end=" ")
    print()