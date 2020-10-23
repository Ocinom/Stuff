import collections

class node():

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def pathSum(self, root: node, sum: int) -> int:
        mp = collections.defaultdict(int)
        mp[0] = 1
        return self.helper(root, mp, 0, sum)

    def helper(self, root, mp, rsum, target):
        if root is None:
            return 0
        rsum += root.val
        calc = rsum - target
        total = mp[calc]
        mp[rsum] += 1
        total += self.helper(root.left, mp, rsum, target)
        total += self.helper(root.right, mp, rsum, target)
        mp[rsum] -= 1
        return total