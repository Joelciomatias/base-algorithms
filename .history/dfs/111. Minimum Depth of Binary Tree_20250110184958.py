from pydoc import visiblename
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

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        res = 0
        def dfs(node, s=0):
            nonlocal res
            if not node:
                return 
            
            if not node.left and not node.right:
                res = min(res, s+1)
            
            dfs(node.left, s+1)         
            dfs(node.right, s+1)
            return res

            
        s = dfs(root)
        return s
            
tree = build_tree([3,9,20,None,None,15,7])  # 2

solution = Solution()
result = solution.maxDepth(tree)
print("Preorder Traversal Result:", result)
