def ebs(n, p):
    if p < 0:
        return ebs(1 / n, -p)
    if p == 0:
        return 1
    if p == 1:
        return n
    if p % 2 == 0:
        return ebs(n * n, p / 2)
    else:
        return n*ebs(n * n, (p - 1) / 2)

print(ebs(2, 10))