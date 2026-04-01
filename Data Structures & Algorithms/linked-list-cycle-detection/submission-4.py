# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        cur = head
        index = []
        while cur.next:
            index.append(cur)
            cur = cur.next
            if cur in index:
                return True
        return False
