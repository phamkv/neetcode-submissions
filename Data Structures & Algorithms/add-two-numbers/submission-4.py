# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        overflow = 0
        while l1 and l2:
            sumD = l1.val + l2.val
            curr.next = ListNode((sumD % 10) + overflow)
            overflow = 1 if sumD > 9 else 0
            l1 = l1.next
            l2 = l2.next
            curr = curr.next
        while l1:
            sumD = l1.val + overflow
            curr.next = ListNode(sumD % 10)
            overflow = 1 if sumD > 9 else 0
            l1 = l1.next
            curr = curr.next
        while l2:
            sumD = l2.val + overflow
            curr.next = ListNode(sumD % 10)
            overflow = 1 if sumD > 9 else 0
            l2 = l2.next
            curr = curr.next
        if overflow == 1:
            curr.next = ListNode(1)
        return dummy.next