# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        index = length - n
        if index == 0:
            return head.next
        prev, curr = None, head
        while index > 0:
            prev = curr
            curr = curr.next
            index -= 1
        prev.next = curr.next
        return head