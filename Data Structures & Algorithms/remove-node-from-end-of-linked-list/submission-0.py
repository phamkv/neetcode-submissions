# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        node = head
        while node:
            node = node.next
            length += 1
        index = length - n + 1
        prev = None
        node = head
        while index > 1:
            prev = node
            node = node.next
            index -= 1
        if not prev:
            return node.next
        prev.next = node.next
        return head
