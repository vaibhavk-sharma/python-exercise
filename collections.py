###### Special Collections: Counter, namedtuple, OrderedDict, defaultdict, deque #####
from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

# Counter: creates a tuple of dictionary with items as key and their count as value
my_str = "vaibhavsharma"
my_counter = Counter(my_str)
# print(my_counter)
# print(list(my_counter))
# print(my_counter.values())

#deque: mutable, double ended queue. An efficient version of list to perform append and pop as thread safe and memory efficient
# No slicing, 
# List vs deque: list better for random access and fixed length operations.deque is optimized for operating on either side of collection. 

