from functools import reduce

#use of map(fonction, iterable)
counters = [1, 3, 4, 5]
updated = []
for x in counters:
    updated.append(x + 10)
print(updated)

def inc(x): return x + 10
print(list(map(inc, counters)))

L = list(map((lambda x: x + 10), counters))
print(L)

#use of filter
print(list(filter((lambda x: x >= 0), range(-10, 10))))

#use of reduce
print(reduce((lambda x, y: x + y), counters))

def myreduce(function, sequence):
    first = sequence[0]
    for next in sequence[1:]:
        first = function(first, next)
    return first

print(myreduce((lambda x, y: x + y), counters))