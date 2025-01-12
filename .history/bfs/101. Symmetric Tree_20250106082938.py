import queue
from typing import Optional

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
    def isSymmetric(self, root: Optional[TreeNode]) -> int:
        
        from collections import deque

        def bfs(root):
            if not root:
                return

            q = deque([root])
            visited = {}
            vi_arr = []

            while q:
                curr = q.popleft()
                if curr not in visited:
                    visited[curr] = True
                    vi_arr.append(curr.val)
                if curr.left is not None:
                    q.append(curr.left)
                if curr.right is not None:
                    q.append(curr.right)
            return vi_arr
        
        if not root.left or not root.right:
            return False
        return bfs(root.left) == bfs(root.right)
            
tree = build_tree([1,2,2,3,4,4,3])

solution = Solution()
result = solution.isSymmetric(tree)
print("isSymmetric", result)
