# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ls = []
        for head in lists:
            while head:
                ls.append((head.val, head))
                head = head.next
        ls.sort(key = lambda x: x[0])
        dummy = cur = ListNode()
        for i in range(len(ls)):
            cur.next = ls[i][1]
            cur = cur.next
        return dummy.next
                