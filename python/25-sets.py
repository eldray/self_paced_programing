#set = collection hic is unordered, ubindexed and no duplicates
#uses {}
utensils = {"fork", "spoon", "knife", "spoon", "saucer"}
print(utensils)

for i in utensils:
    print(i)

#methods
utensils.add("napkin")
print(utensils)
utensils.remove("fork")
print(utensils)
utensils.clear()
print(utensils)

#adding a new set
dishes={"bowl", "plate", "cup"}
utensils.update(dishes)

#joining two different sets
dishes={"bowl", "plate", "cup"}
utensils = {"fork", "spoon", "knife", "spoon", "saucer"}
dinner_table = utensils.union(dishes)
print(dinner_table)


dishes={"bowl", "plate", "cup", "fork", "spoon"}
utensils = {"fork", "spoon", "knife", "spoon", "saucer"}
#find an item which is not in the other set
print(utensils.difference(dishes))

#find an item which is present in both sets
print(utensils.intersection(dishes))