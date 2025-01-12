
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_symmetric_tree(levels):
    if levels == 0:
        return None
    
    root = TreeNode(1)
    current_level = [root]
    value = 2
    
    for _ in range(levels - 1):
        next_level = []
        for node in current_level:
            node.left = TreeNode(value)
            node.right = TreeNode(value)
            value += 1
            next_level.append(node.left)
            next_level.append(node.right)
        current_level = next_level
    
    return root

def print_tree(root, level=0, prefix="Root: "):
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.val))
        print_tree(root.left, level + 1, "L--- ")
        print_tree(root.right, level + 1, "R--- ")


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
        
        def dfs(l, r):
            if not l and not r:
                return True
            if not l or not r:
                return False
            
            return (l.val == r.val and \
                    dfs(l.left, l.right) and dfs(l.right, l.right))
                
        return dfs(root.left, root.right)
                

        # from collections import deque

        # def bfs(root):
        #     if not root:
        #         return

        #     q = deque([root])
        #     visited = {}
        #     vi_arr = []
        #     s = {}
        #     d = 1

        #     while q:
        #         curr = q.popleft()
        #         if curr not in visited:
        #             visited[curr] = True
        #             vi_arr.append(curr.val)

        #         if curr.left is not None:
        #             q.append(curr.left)
        #         if curr.right is not None:
        #             q.append(curr.right)
        #         l = curr.left.val if curr.left else None
        #         r = curr.right.val if curr.right else None
        #         s[d, l, r] = l == r
        #         d += 1
        #     t = len(vi_arr)-1
        #     c = 0
        #     for i in range(1, t):
        #         if i + c > t:
        #             return

        #         print(vi_arr[i], vi_arr[i+c])
        #         c += 1
            
        #     return vi_arr
        
        # if not root.left or not root.right:
        #     return False
        # # arr1 = bfs(root.left) 
        # # arr2 = bfs(root.right)
        # # print(arr1,arr2)
        # bfs(root)
        # return 1==1
            
tree = build_tree([1,2,2,3,4,4,3])

# tree = build_tree([1,2,2,None,3,None,3])

solution = Solution()
result = solution.isSymmetric(tree)
print("isSymmetric", result)


