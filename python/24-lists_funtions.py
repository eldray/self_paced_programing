#list = used to store a multiple items in a simple variable

food = ["Rice", "Noodles", "Kenkey", "Fufu", "Waakye", "Jollof"]
#replacing an item in a list
food[1]="indomie"
print(food[1])
print(food)

food.append("Ice-cream")
print(food)

food.remove("Fufu")
print(food)

food.pop() #removes the last item in the list
print(food)

food.insert(0, "Cake") #inserts an item to the front
print(food)

food.sort() #sorts the list aphabtically
print(food)

food.clear() #deletes the entire lists
print(food)

