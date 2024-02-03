def _sum(L):
    if not L:
        return 0
    else:
        return L[0] + _sum(L[1:])
    
print(_sum([1,2,3,5]))

def _sum1(L):
    return 0 if not L else L[0] + _sum(L[1:])

print(_sum1([1,3,4,4]))