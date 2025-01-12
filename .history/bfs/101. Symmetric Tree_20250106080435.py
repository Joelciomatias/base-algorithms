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

        d = deque([1, 2, 3])

        # Adicionando elementos
        d.append(4)       # Adiciona ao final
        d.appendleft(0)   # Adiciona ao início

        # Removendo elementos
        i = d.pop()           # Remove do final
        d.popleft()       # Remove do início

        print(d)

        while True:
            


        return False
            
tree = build_tree([[1,2,2,3,4,4,3]])

solution = Solution()
result = solution.isSymmetric(tree)
print("isSymmetric", result)
