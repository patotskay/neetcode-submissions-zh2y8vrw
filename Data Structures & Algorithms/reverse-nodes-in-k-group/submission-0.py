# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
       # 1. Проверяем, есть ли у нас k узлов, чтобы их развернуть
        curr = head
        count = 0
        while curr and count < k:
            curr = curr.next
            count += 1
        
        # Если узлов меньше k, оставляем их как есть (по условию задачи)
        if count < k:
            return head
        
        # 2. Разворачиваем k узлов
        prev = None
        curr = head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # 3. Рекурсивно вызываем для остальной части списка
        # Теперь head — это хвост развернутой группы
        head.next = self.reverseKGroup(curr, k)
        
        # prev — это новая голова развернутой группы
        return prev


