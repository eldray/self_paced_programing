#slicing = create a string by extracting elements from another
# indexing[] 0r slice()
#[start:stop:step]

name = "EmmanuelAppiah"
first_name = name[0:9]
last_name = name[5:9]
funky_name = name[0:8:1]
funky_name2 = name[0:14:2]
reversed_name = name[::-1]
print(first_name)
print(last_name)
print(funky_name)
print(funky_name2)
print(reversed_name)

#slicing
website1 = "https://google.com"
website2 = "https://wikipedia.com"

slice = slice(8, -4)

print(website1[slice])
print(website2[slice])