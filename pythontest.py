
# List: ordered, mutable, allows duplicate
list1 = ["Vaibhav", 0, "Sharma"]
list1.reverse()
# print(list1)

#  Tuples - ordered, immutable, allows duplicates. more efficient than list
my_tuple = ("Vaibhav", 0, "Sharma")

# Dictionary: Unordered, mutable, key value pair
my_dictionary = {"firstname": "Vaibhav", "surname": "Sharma"}
# print(my_dictionary.get("surname"))
# print(my_dictionary["surname"])

# Sets : unordered, mutable, no duplicates
my_set = {1, 2, 3, 4}
my_set2 = {3, 4, 5, 6}
# print(my_set)
# print(my_set.difference(my_set2))
# print(my_set2)
# frozenset: Immutable set
my_frozenset = frozenset([1, 2, 3, 4])

# Strings: Ordered, Immutable
my_str = "Vaibhav Sharma"
my_int = 35.5
# print(my_str[::-1]) # Reverse trick
my_list_to_join = ["you", "are", "good"]
# print(' '.join(my_list_to_join))  # Trick to join a list items
# print(f"my name is {my_str} and age is {int(my_int)}")
