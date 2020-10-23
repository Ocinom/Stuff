memo = {}

def memoize(N: int) -> int:
    if N in memo:
        return memo[N]
    memo[N] = memoize(N - 1) + memoize(N - 2)
    return memo[N]

def fib(N: int) -> int:
        if N == 1 or N == 2:
            return 1
        memo = {0: 0, 1: 1}
        return memoize(N)

print(fib(5))