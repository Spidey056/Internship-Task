# Creating a set
print("Creating a set")
my_set = {1, 2, 3, 4, 5}
print(my_set)
print("-------------------------")


# Set Bulid-in Methods
print("Set Bulid-in Methods")
my_set.add(4)
print(f"After Adding: {my_set}")
my_set.remove(2)
print(f"After Removing: {my_set}")
my_set.discard(5)
print(f"After Discarding: {my_set}")
popped_element = my_set.pop()
print(f"Popped Element: {popped_element}")
print("-------------------------")


# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(f"Union: {union_set}")
intersection_set = set1.intersection(set2)
print(f"Intersection: {intersection_set}")
difference_set = set1.difference(set2)
print(f"Difference: {difference_set}")
print("-------------------------")


#Frozen Set
print("Frozen Set")
frozen_set = frozenset([3,4,5])
print(frozen_set)
print("-------------------------")


# Clearing all elements from a set
print("Clearing a set")
my_set.clear()
print(my_set)
print("-------------------------")