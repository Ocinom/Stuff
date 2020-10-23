# Thanks G4G.

# The binary search algorithm goes as follows: in a sorted array,
# Calculate the mid-point. If the mid-point is greater than the desired
# Value, perform the same search in the lower half (minus the mid-point)
# If it is greater, do it in the upper half (minus the mid-point)

# This recursion ends on one of two conditions: The mid-point matches
# A value at some point in the recursion, and the index of that value is
# Returned. OR There is no solution and the value of right is eventually
# Overtaken by left, at which point a False value is returned (-1 if you
# want an integer)

def bins(arr, left, right, res):

    if right >= left:

        mid = (left + right) // 2

        if arr[mid] == res:
            return mid

        elif arr[mid] > res:
            print(arr[mid])
            return bins(arr, left, mid - 1, res)

        elif arr[mid] < res:
            return bins(arr, mid + 1, right, res)

    else:
        return False

test = [i for i in range(100)]

print(bins(test, 0, len(test) - 1, 10))