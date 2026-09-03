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
        if not head:
            return None
        copyMap = {}
        node = head
        prev = None
        while node:
            copyMap[node] = Node(node.val)
            if prev:
                copyMap[prev].next = copyMap[node]
            prev = node
            node = node.next
        node = head
        while node:
            if node.random:
                copyMap[node].random = copyMap[node.random]
            else:
                copyMap[node].random = None
            node = node.next
        return copyMap[head]