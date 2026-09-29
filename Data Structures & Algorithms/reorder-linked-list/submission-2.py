# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_head = slow.next
        slow.next = None
        prev = None
        curr = second_head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        second_head = prev
        first_head = head
        while second_head:
            tmp1, tmp2 = first_head.next, second_head.next
            first_head.next = second_head
            second_head.next = tmp1
            first_head, second_head = tmp1, tmp2
        
