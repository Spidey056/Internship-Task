# Creating a list
print("Creating a List")
my_list_1 = [1, 2, 3, 'apple', 'banana', 'cherry']
my_list_2 = list(range(6))
print(my_list_1)
print(my_list_2)
print(type(my_list_1))
print("-------------------")


# Indexing
print("Indexing")
print(my_list_1[4])
print(my_list_2[-1])
print("-------------------")


# Slicing
print("Slicig")
subset = my_list_1[1:4]
print(f"SubList: {subset}")
print("-------------------")


# Modifying elements
print("Modifying Elements")
my_list_1[2] = 'orange'
my_list_1.append('grape')
print(f"List After Modification: {my_list_1}")
print("-------------------")


# List methods
print("List Bulid-in Methods")
length = len(my_list_1)
print(f"Length of the list: {length}")
my_list_1.insert(2, 'peach')
print(f"List After Insertion : {my_list_1}")
removed_item = my_list_1.pop(4)
print(f"Removed Items: {removed_item}")
my_list_1.remove('banana')
sorted_list = sorted(f"List After Removal: {my_list_1}")
print("-------------------")


# List comprehension
print("List Comprehension")
multiples_of_2 = [x*2 for x in range(1,6)]
print(multiples_of_2)
print("-------------------")


# Nested lists
print("Nested Lists")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)
print("-------------------")


# Check if an element exists in the list
print("Checking if exist")
is_present = 'orange' in my_list_1
print(is_present)
print("-------------------")


# Clearing the entire list
print("Clearing the list")
my_list_1.clear()
print(f"After Clearing the list : {my_list_1}")
print("-------------------")