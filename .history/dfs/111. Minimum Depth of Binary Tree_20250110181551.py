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
        def dfs(l, r):
            if not l and not r:
                return True
            if not l or not r:
                return False
            
            res =  (l.val == r.val and \
                    dfs(l.left, r.right) and dfs(l.right, r.left))
            return res
                
        return dfs(root.left, root.right)

            
# tree = build_tree([3,9,20,None,None,15,7])  # 2
tree = build_tree([2,None,3,None,4,None,5,None,6])  # 5



solution = Solution()
result = solution.maxDepth(tree)
print("Preorder Traversal Result:", result)
