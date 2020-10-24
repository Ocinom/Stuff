# Recursive. Pretty bad ngl. DP/iterative/tail recursion?

#def fact(n):
#    if n == 0:
#        return 1
#    if n == 1:
#        return n
#    if n > 1:
#        return n * fact(n - 1)

#print(fact(5))

def fact(n):
    res = 1
    if n == 0 or n == 1:
        return 1
    for i in range(1, n + 1):
        res *= i
       return res
