# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        cur = head
        d = {}
        i = 0
        while cur:
            d[i] = cur
            cur = cur.next
            i += 1
        right = i - 1
        left = 0
        dummy = ListNode()
        cur = dummy
        while right >= left:
            cur.next = d[left]
            cur = cur.next
            left += 1
            if right >= left:
                cur.next = d[right]
                cur = cur.next
                right -= 1
        cur.next = None 
        

            