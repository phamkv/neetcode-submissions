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
        
        curr = head
        while curr:
            newNode = Node(curr.val)
            newNode.next = curr.next
            curr.next = newNode
            curr = curr.next.next
        
        curr = head
        while curr:
            newNode = curr.next
            if curr.random:
                newNode.random = curr.random.next
            curr = curr.next.next
        
        newHead = head.next
        curr = head
        while curr:
            newNode = curr.next
            curr.next = newNode.next
            if newNode.next:
                newNode.next = newNode.next.next
            curr = curr.next

        return newHead