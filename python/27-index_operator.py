# index operator [] = gives access to a sequence's element(str, list, tuples)

name ="shine FEEL%"

if (name[0].islower()):
    name = name.capitalize()
print(name)

first_name = name[0:6].upper()
print(first_name)

last_name = name[6:].lower()
print(last_name)

last_char = name[-1]
print(last_char)