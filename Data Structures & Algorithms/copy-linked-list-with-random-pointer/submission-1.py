"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodeToCopy = {None: None}
        curr = head
        while curr:
            nodeToCopy[curr] = Node(curr.val)
            curr = curr.next
        dummy = Node(0, nodeToCopy[head])
        curr = head
        while curr:
            copyCurr = nodeToCopy[curr]
            copyCurr.next = nodeToCopy[curr.next]
            copyCurr.random = nodeToCopy[curr.random]
            curr = curr.next
        return dummy.next