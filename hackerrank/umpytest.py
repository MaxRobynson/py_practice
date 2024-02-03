import numpy

n = input().split()
n = list(map(float, n))
arr = numpy.array(n)
print(numpy.floor(arr))
print(numpy.ceil(arr))
print(numpy.rint(arr))