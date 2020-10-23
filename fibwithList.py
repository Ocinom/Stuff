import time



def fib(n):
    cache = []
    for i in range(n):
        if i == 0 or i == 1:
            cache.append(1)
            continue
        cache.append(cache[-1] + cache[-2])
    return cache[-1]

start = time.time()
print(fib(50))
end = time.time()

print(end - start)