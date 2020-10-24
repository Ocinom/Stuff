import time
from random import randint as r

v = r(0, 500)
print('v:   {0}'.format(v))
a = [r(0, 500) for i in range(10)]
a.sort()
print(a)

l = 0
r = len(a) - 1
mid = len(a) // 2
count = 0

start = time.time()
while l <= r:
    print('{0}  |  {1}'.format(l, r))

    if l == r:
        print('{0} is between {1} and {2}'.format(v, a[r], a[r - 1]))
        break

    if a[mid] == v:
        print(a[mid])
        break

    if a[mid] > v:
        r = mid
        mid = (l + r) // 2

    if a[mid] < v:
        l = mid + 1
        mid = (l + r) // 2

end = time.time()

print('time taken: {0}'.format(end - start))
