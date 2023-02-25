# str.format() = a format method available to strings
# gives more control when displaying an output

animal = "cow"
item = "moon"

text = "The {} jumped over the {}"
print(text.format(animal,item))
print(text.format(item,animal))