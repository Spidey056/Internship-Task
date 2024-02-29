# Creating a tuples
print("Creating a Tuples")
my_tuple = (1, 2, 3, 'hello', 3.14)
my_tuple2 = (4, 5, 6)
print(my_tuple)
print(my_tuple2)
print("----------------------------")

# Indexing
print("Indexing")
print(my_tuple[0])
print(my_tuple[3])
print("----------------------------")


# Slicing a tuples
print("Slicing")
slice_of_tuple = my_tuple[1:4]
print(slice_of_tuple)
print("----------------------------")


# Arithmetic Operators in Tuplels
concatenated = my_tuple + my_tuple2
repeated = my_tuple * 3
print(f"Concatenated: {concatenated}")
print(f"Repeated: {repeated}")
print("----------------------------")


# Tuples unpacking
print("Tuples Unpacking")
a, b, c, d, e = my_tuple
print(a, b, c, d, e)
print("----------------------------")


# Checking if an element exists in a tuple
print("Checking if Exists")
print('hello' in my_tuple)
print('python' in my_tuple)
print("----------------------------")

# Tuples Bulid-in Functions
print("Tuples Bulid-in Functions")
count_of_2 = my_tuple.count(2)
index_of_hello = my_tuple.index('hello')
print(index_of_hello)
print(count_of_2)
print("----------------------------")