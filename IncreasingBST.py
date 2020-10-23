def increasingBST(root, tail = None):
        if not root: return tail
        res = increasingBST(root.left, root)
        root.left = None
        root.right = increasingBST(root.right, tail)
        return res