import numpy

"""my_array = numpy.array([ [1, 2], [3, 4] ])

print(numpy.sum(my_array, axis = 0) )        #Output : [4 6]
print( numpy.sum(my_array, axis = 1))        #Output : [3 7]
print(numpy.sum(my_array, axis = None) )     #Output : 10
print( numpy.sum(my_array) )                  #Output : 10
print(numpy.prod(my_array, axis = 0)   )         #Output : [3 8]
print(numpy.prod(my_array, axis = 1))            #Output : [ 2 12]
print(numpy.prod(my_array, axis = None))         #Output : 24
print(numpy.prod(my_array))                      #Output : 24"""

import numpy as np

# Input: Reading N and M
n, m = map(int, input().split())

# Reading the 2-D array
arr = np.array([input().split() for _ in range(n)], dtype=int)
print(arr)
# Calculating the sum along axis 0
sum_result = np.sum(arr, axis=0)

# Calculating the product of the sum
product_result = np.prod(sum_result)

# Printing the result
print(product_result)
