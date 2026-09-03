# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        tmp = slow.next
        slow.next = None
        slow = tmp
        
        prev = None
        curr = slow
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        curr1, curr2 = head, prev
        while curr1 and curr2:
            tmp1, tmp2 = curr1.next, curr2.next
            curr1.next = curr2
            curr2.next = tmp1
            curr1, curr2 = tmp1, tmp2
        
        