def MaxContiguous(arr):
    mx = 0
    cur = 0
    for i in arr:
        if cur + i < 0:
            mx = cur
            cur = 0
            continue
        cur += i
        if cur > mx:
            mx = cur
    return mx

print(MaxContiguous([34, -50, 42, 14, -5, 86]))