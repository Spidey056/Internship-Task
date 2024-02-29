# Creating a dictionary
print("Creating a Dictionary")
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
print(my_dict)
print("--------------------------")


# Accessing values using keys
print("Indexing using Keys")
print(my_dict['name'])
print(my_dict['age'])
print("--------------------------")


# Dictionary Operations
print("Dictionary Operations")
my_dict['age'] = 26
print(f"Modifiying Dictionary: {my_dict}")
my_dict['gender'] = 'Male'
print(f"Adding a Key with Value: {my_dict}")
del my_dict['city']
print(f"Deleting a Key:Value Pair: {my_dict}")
print("--------------------------")


# Checking if a key exists
print("Checking if key exists")
print('name' in my_dict)  # Output: True
print('city' in my_dict)  # Output: False
print("--------------------------")


# Getting all keys and values
print("Dictionary Bulid-in Functions")
keys = my_dict.keys()
values = my_dict.values()
print(f"Keys: {keys}")
print(f"Values: {values}")
print("--------------------------")


# Iterating through keys and values
print("Iterating a Dictionary")
for key, value in my_dict.items():
    print(f'{key}: {value}')

print("--------------------------")


# Clearing all key-value pairs
print("Clearing a Dictionary")
my_dict.clear()
print(f"After Clearing a Dictionary: {my_dict}")
print("--------------------------")