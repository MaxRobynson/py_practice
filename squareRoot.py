"""x = int(input('enter a number: '))
epsilon = 0.01
step = epsilon**2
num_guesses = 0
ans = 0.0
while abs(ans**2 -x) >= epsilon and ans<= x:
    ans += step
    num_guesses += 1
print('number of guess', num_guesses)
if abs(ans**2 -x ) >= epsilon:
    print('Failed on square root of', x)
else:
    print(ans, 'is close to square root of', x)


##bisection search to approximate square root of an integer
def approxSquare(x, epsilon):
    #epsilon = 0.01
    if x < 0:
        print('Does not exist')
    else:
        low = 0
        high = max(1, x)
        ans = (high + low)/2
        while abs(ans**2 -x) >= epsilon:
            if ans**2 < x:
                low = ans
            else:
                high = ans
            ans =(high +low)/2
        print(ans, 'is close to square root of ', x)
approxSquare(2, 0.001)"""

def find_root(x, power, epsilon):
    #trouver l'interval contenat answer: ans
    if x < 0 and power%2 == 0:
        return None #Negative number has no even -powerd roots
    low = min(-1, x)
    high = max(1, x)
    #using bisection search
    ans = abs(high +low)/2
    while abs(ans**power - x) >= epsilon:
        if ans**power < x :
            low = ans
        else:
            high =ans
        ans = (high + low)/2
    return ans

print(find_root(100, 2, 0.01))

print('sum : ', find_root(25,2,0.001)+ find_root(-8,3,0.001)+ find_root(16,4,0.001))

def test_find_root(x_vals, powers, epsilons):
    for x in x_vals:
        for p in powers:
            for e in epsilons:
                result = find_root(x, p, e)
                if result == None:
                    val = 'No root exist'
                else:
                    val = 'Okay'
                    if abs(result**p - x) > e:
                        val = 'Bad'
                print(f'x = {x}, power = {p}, epsilon = {e}: {val}')

x_vals = (0.25, 8, -8)
powers = (1,2,3)
epsilons = (0.1, 0.001, 1)
test_find_root(x_vals, powers, epsilons)