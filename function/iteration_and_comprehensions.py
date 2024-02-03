#map vs list comprehension
txt = 'spam'
res = []
for x in txt:
    res.append(ord(x))
print(res)

res1 = list(map(ord, txt))
print(res1)

res2 = [ord(x) for x in txt]
print(res2)

# list comprehension as filter
print([ x for x in range(-5,5) if x > 0])
print(list(filter((lambda x: x > 0), range(-5,5))))

# list comprehension as filter and map
print([ x**2 for x in range(5) if x % 2 == 0])
print(list(map((lambda x: x**2), filter((lambda x: x % 2 ==0), range(5)))))

#nested list comprehension
print([ x + y for x in [1,2,3] for y in [100, 200, 300]])
res = []
for x in [1,2,3]:
    for y in [100,200,300]:
        res.append(x+y)
print(res)


#List comprehension and matrix

M = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]
N = [[2, 2, 2],
     [3, 3, 3],
     [4, 4, 4]]
print("Accessing the diagonal:", [M[i][i] for i in range(len(M))])

res = []
for i in range(len(M)):
    res.append(M[i][i])
print(res)

#multiplication  matrix simple
print('mulpication: ', [ M[row][col] * N[row][col] for row in range(3) for col in range(3)])
print('mulpication nested: ', [ [M[row][col] * N[row][col] for col in range(3)] for row in range(3)])
