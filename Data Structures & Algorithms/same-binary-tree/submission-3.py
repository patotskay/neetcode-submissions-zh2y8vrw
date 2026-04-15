# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.ans = []
        self.counter = 0
        def dfs(node):
            if not node:
                return
            if not node.left or not node.right:
                self.ans.append(None)
            dfs(node.left)
            self.ans.append(node.val)
            dfs(node.right)
            
        dfs(p)
        self.p = self.ans
        self.ans = []
        self.counter = 0
        dfs(q)
        print(self.p, self.ans)
        return self.p == self.ans    
