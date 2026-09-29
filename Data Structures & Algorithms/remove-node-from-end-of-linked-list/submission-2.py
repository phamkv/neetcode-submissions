# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        dummy = ListNode(0, head)
        slow = fast = dummy
        k = 0
        while k < n:
            fast = fast.next
            k += 1
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next