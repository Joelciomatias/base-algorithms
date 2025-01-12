# Definition for singly-linked list.
from typing import Optional


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        s = set()
        def f(nd):
            if not nd:
                return False
            if nd.val in s:
                return True
            s.add(nd.val)
            f(nd.next)
        
        return f(head)
        