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


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        res = 0
        first = None
        last = None
        def dfs(nd, c=0):
            if not nd:
                return
            if first:
                c += 1
            if not nd.left and not nd.right and not first:
                first = nd
            elif not nd.left and not nd.right and first:
                last = nd

            dfs(nd.left)
            dfs(nd.right)
                
        dfs(root)
        return root