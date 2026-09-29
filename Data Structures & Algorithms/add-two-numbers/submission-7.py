# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy

        overflow = 0
        while l1 and l2:
            summation = l1.val + l2.val + overflow
            if summation > 9:
                overflow = 1
                summation = summation % 10
            else:
                overflow = 0
            curr.next = ListNode(summation)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        
        biggerList = l1 if l1 else l2
        while biggerList:
            summation = biggerList.val + overflow
            if summation > 9:
                overflow = 1
                summation = summation % 10
            else:
                overflow = 0
            curr.next = ListNode(summation)
            curr = curr.next
            biggerList = biggerList.next
        if overflow == 1:
            curr.next = ListNode(overflow)
        return dummy.next

