# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if  l1.val == 0 and l2.val == 0:
            head = ListNode()
            head.val = 0
            head.next = None
            return head
        num1 = ""
        num2 = ""
        if l1.val != 0:
            cur = l1
            while cur:
                num1 += str(cur.val)
                cur = cur.next
        else:
            num1 = "0"
        if l2.val != 0:
            cur = l2
            while cur:
                num2 += str(cur.val)
                cur = cur.next
        else:
            num2 = "0"
        num = int(num1[::-1]) + int(num2[::-1])
        cur = dummy = ListNode()
        while num != 0:
            
            cur.next = ListNode()
            cur = cur.next
            cur.val = num % 10
            num = num // 10
        cur.next = None
        return dummy.next
            