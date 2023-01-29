# itertools: advance operations on iterators (list, etc.): product, permutations, combinations, accumulate, groupby, infinite
from itertools import product, permutations, combinations, accumulate, groupby, count, cycle, repeat
import operator

#product: cartesian product.
my_list = [1,2]
my_tuple = (3,4)

product = product(my_list,my_tuple)
#print(list(product))

#permutations: All possible permutations
perm = permutations(my_list)
#print(list(perm))

# accumulate: accumulates the sum or multiplication with next number
my_list1 = [1,2,35,6]
accu = accumulate(my_list1, func=operator.mul) # 1*1, 1*2, 2*35, 70*6 
#print(list(accu)) #[1, 2, 70, 420]

# groupby: you can group by the list items based on some key
employees = [{'name': 'Ram', 'salary':500}, {'name':'Shyam', 'salary':1000}, {'name':'Param', 'salary':500}, 
                {'name':'Karam', 'salary':1000}, {'name':'Kesar', 'salary':6000}]
group_by_sal = groupby(employees, key=lambda x:x['salary']>3000)
#for key, value in group_by_sal:
    #print(key, list(value))
    #False [{'name': 'Ram', 'salary': 500}, {'name': 'Shyam', 'salary': 1000}, {'name': 'Param', 'salary': 500}, {'name': 'Karam', 'salary': 1000}]
    #True [{'name': 'Kesar', 'salary': 6000}]

# count: generate counts till infinite, cycle: generates inifinte cycles of a list items, repeat: repeats the item infinte times
# a = [1,2,3]
# for i in count(10):
#     print(i)
#     if(i>15):
#         break;


