
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(data):
    if not data or data[0] is None:
        return None
    
    nodes = [TreeNode(val) if val is not None else None for val in data]
    kids = nodes[::-1]
    root = kids.pop()
    
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.res = 0
        
        def dfs(nd):
            if not nd:
                return 0
            
            left = dfs(nd.left)
            right = dfs(nd.right)

            self.res = max(self.res, left + right)
            return 1 + max(left, right)
                
        dfs(root)
        return self.res

tree = build_tree([1,2,3,4,5])

solution = Solution()
result = solution.diameterOfBinaryTree(tree)
print("diameterOfBinaryTree:", result)