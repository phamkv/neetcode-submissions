# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = ListNode()
        result = curr
        carry = val1 = val2 = 0
        while l1 or l2:
            val1 = 0 if not l1 else l1.val
            val2 = 0 if not l2 else l2.val
            s = val1 + val2 + carry
            carry = 1 if s > 9 else 0
            curr.next = ListNode(s % 10)
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry > 0:
            curr.next = ListNode(1)
        return result.next
            


