def pow(x, n):
        if n == 0:
            return 1
        if n % 2 == 0:
            return pow(x * x, n // 2)
        else:
            return x * pow(x, n // 2) * pow(x, n // 2)

def myPow(x: float, n: int) -> float:
    if n < 0:
        return 1 / myPow(x, -n)

    return pow(x, n)

print(myPow(2, 10))