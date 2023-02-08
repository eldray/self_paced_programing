#tuple = collection which is ordered and unchangeable
#used to group together related items

student = ["Emmanuel", "Appiah", 30, "Male", "Programmer", "Mercedes"]

print(student)
#functions available in tuple
print(student.count("Emmanuel"))
print(student.index("Male"))
print(student.pop())

#using for loop
for x in student:
    print(x)

#if statements
if "Bro" != student:
    print("Not found")

if "Emmanuel" in student:
    print("Emmanuel is here")
