Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import m a t pl o tli b . p y pl o t a s p l t
x = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 1 0]
y = [ 5 , 2 , 4 , 4 , 8 , 7 , 4 , 8 , 1 0 , 9 ]
p l t . pl o t ( x , y )
p l t . x l a b e l ( ’Time ( s ) ’ )
p l t . y l a b e l ( ’ Temperature ( degC) ’ )
p l t . show ( )
SyntaxError: invalid character '’' (U+2019)
import matplotlib.pyplot as plt

x = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 1 0]

y = [ 5 , 2 , 4 , 4 , 8 , 7 , 4 , 8 , 1 0 , 9 ]

plt.plot( x , y )
plt.xlabel( 'Time ( s )')
plt.ylabel( 'Temperature ( degC)')
plt.show( )
SyntaxError: multiple statements found while compiling a single statement
print(2)
2
def fibo(n):
    fib = [0,1]
    for i in range(n-2):
        fibNext = fib[i+1]+fib[i]
        fib.append(fibNext)
    print(fib)

    
fib(5)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    fib(5)
NameError: name 'fib' is not defined. Did you mean: 'fibo'?
fibo(5)
[0, 1, 1, 2, 3]
fibo(12)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
