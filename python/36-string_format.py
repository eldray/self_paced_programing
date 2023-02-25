# str.format() = a format method available to strings
# gives more control when displaying an output

# case scenario
animal = "cow"
item = "moon"

#print("The " + animal+ " jumped over the " + item)

#using str.format
# the {} serves as a placeholder for the variables
print("The {} jumped over the {}".format("cow", "moon")) # using values
print("The {} jumped over the {}".format(animal, item)) # using varibales
print("The {1} jumped over the {0}".format(animal, item)) # positional argument
print("The {0} jumped over the {1}".format(animal, item)) # positional argument
print("The {animal} jumped over the {item}".format(animal="cow", item="moon")) #kwargs