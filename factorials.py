def factorial_iterative(n):
    result = 1
    for i in range(1,n+1):
        result = result * i
    return result

def factorial_recursive(n):
    if n >= 1:
        return n * factorial_recursive(n-1)
    else:
        return 1

t1 = 5
print('test: ', t1, 'it: ', factorial_iterative(t1), 'rec: ', factorial_recursive(t1))