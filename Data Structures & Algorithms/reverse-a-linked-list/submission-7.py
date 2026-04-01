# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_temp = None
        current = head
        while current:
            next_temp = current.next
            current.next = prev_temp
            prev_temp = current
            current = next_temp
        return prev_temp