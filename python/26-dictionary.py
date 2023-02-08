#dictionary = changeable, o=unordered collection of unique key value pairs
# fast because they use hashing, allow accese to a value quickly

capitals = {'USA':'Washington DC',
            'India':'New Delhi',
            'Ghana':'Accra',
            'Nigeria':'Abuja',
            'China': 'Beijing'}
print(capitals)
print(capitals['Ghana'])
#print(capitals['Germany']) #prints an error

#use get method
print(capitals.get('Germany'))

#methods
print(capitals.keys())
print(capitals.values())
print(capitals.items())

#using for loop
for keys in capitals:
    print(keys)
#print the whole items
for key,value in capitals.items():
    print(key, value)

#adding a new item
capitals.update({'Germany':'Berlin'})
print(capitals)
#udating an existing item
capitals.update({'Nigeria':'Lagos'})
print(capitals)

#removing an item
capitals.pop('China')
print(capitals)

#deleting the entire dictionary
capitals.clear()
print(capitals)