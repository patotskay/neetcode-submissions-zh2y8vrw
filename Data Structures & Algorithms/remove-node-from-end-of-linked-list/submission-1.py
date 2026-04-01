# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return 
        cur = head
        i = 0
        d = {}
        while cur:
            d[i] = cur
            cur = cur.next
            i += 1
        cur = dummy = ListNode()
        j = 0
        if n == 1:
            while j != i:
                if j != i - 1:
                    cur.next = d[j]
                    cur = cur.next
                    j += 1
                else:
                    cur.next = None
                    j += 1
        elif i - n + 1 != 0:
            while j != i:
                if j != i - n:
                    cur.next = d[j]
                    cur = cur.next
                    j += 1
                else:
                    cur.next = d[j]
                    j += 1
            
        return dummy.next
