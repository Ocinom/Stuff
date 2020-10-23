class Node():

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse(head, prev=None):
    if not head:
        return prev

    cur, head.next = head.next, prev
    return reverse(cur, head)