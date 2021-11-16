'''https://codereview.stackexchange.com/questions/139620/nth-fibonacci-number-bottom-up-with-dict'''
def memoize(func):
    func.memo = {1: 1, 2: 1}
    return func


@memoize
def Fib(n):
    for i in range(3, n+1):
        Fib.memo[i] = Fib.memo[i-1] + Fib.memo[i-2]
    return Fib.memo[n]

print( Fib(15))
