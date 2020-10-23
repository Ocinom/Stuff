def nats(n):
    yield n
    yield from nats(n + 1)

s = nats(2)

def sieve(s):
    n = next(s)
    yield n
    yield from sieve(i for i in s if i % n != 0)

a = sieve(nats(2))

for i in range(50):
    print(next(a))

