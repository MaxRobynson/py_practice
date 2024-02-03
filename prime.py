def prime(N):
    primes = []
    total = 0
    for i in range(1, N):
        count = 0
        for y in range(1, i+1):
            if i % y == 0:
                count +=1
        if count == 2:
            total += i
            primes.append(i)
    
    return total


    
#print(primes)
print(prime(10))

primes = list(filter(lambda x : all(x % y != 0 for y in range(2, x)), range(2, 10)))
print("is: ",primes)

"""
def check_prime(number):
    if number > 1:
        for i in range(2, number):
            if (number % i )== 0:
                print(number, " is not prime number")
                break
            else:
                print(number, "is prime number")
number = int(input("entern number"))
check_prime(number)"""

"""
num = int(input("insert a number: "))
x = [y for y in range(2, max) if num % y == 0]
def is_prime(n):
    if num > 1:
        if len(x) == 0:
            print("prime")
        else:
            print("NOT prime")
    else:
        print("NOT prime")
is_prime(num)"""


"""def calcaverage(n, m):
    totalsum = n+m
   
    mean = totalsum / 2
    return mean

print(calcaverage(58,6))

from math import pi
def r2d(x):
    
    x = x * (180/pi)
    print(x)

def d2r(x):
    
    x = x * (pi/180)
    print(x)
d2r(45)

r2d(45)"""
