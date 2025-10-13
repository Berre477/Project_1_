from math import sqrt
import numpy as np
list_of_numbers=[x for x in range(10)]






def ecart_type(list_of_numbers):
    pop_mean=sum(list_of_numbers)/len(list_of_numbers)
    list_op=[]
    for x in list_of_numbers:
        list_op.append(((x-pop_mean)**2))
    sum_of_value=sum(list_op)
    return sqrt((sum_of_value/len(list_of_numbers)))
print(np.std([1,2,3,4,5,6,7,8,9,10]))
print(ecart_type([1,2,3,4,5,6,7,8,9,10]))
