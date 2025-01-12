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
        from collections import deque

        def bfs(root):
            if not root:
                return

            q = deque([root])
            visited = {}

            d = 1

            while q:
                curr = q.popleft()
                if curr not in visited:
                    visited[curr] = True

                if curr.left is not None:
                    q.append(curr.left)
                if curr.right is not None:
                    q.append(curr.right)

                d += 1
            return d

        r = bfs(root)
        return r

            
# tree = build_tree([3,9,20,None,None,15,7])  # 2
tree = build_tree([2,None,3,None,4,None,5,None,6])  # 5



solution = Solution()
result = solution.maxDepth(tree)
print("Preorder Traversal Result:", result)
