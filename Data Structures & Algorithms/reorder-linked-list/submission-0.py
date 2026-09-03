# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        tmp = slow.next
        slow.next = None
        slow = tmp
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        result = head
        while head and prev:
            tmp1 = head.next
            head.next = prev
            head = tmp1
            tmp2 = prev.next
            prev.next = tmp1
            prev = tmp2
