# Definition for singly-linked list.
from typing import Optional

from sqlalchemy import true


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Helper function to create a linked list from a list
def create_linked_list(elements, pos=None):
    if not elements:
        return None
    head = ListNode(elements[0])
    current = head
    for val in enumerate(elements[1:]):
        current.next = ListNode(val)
        current = current.next

    ##
    if pos >= 0:
        i = 0
        current = head
        cicle = None
        while current:
            if pos == i:
                cicle = current
            if not current.next:
                current.next = cicle
                break
            current = current.next
            i += 1


    return head


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        res = False
        # s = set()
        # ht = {}
        # def f(nd):
        #     if not nd or not nd.next:
        #         return False
        #     # if nd.val in s:
        #     #     return True
        #     # s.add(nd.val)
        #     k = (nd.val, nd.next.val)
        #     if ht.get(k):
        #         return True
        #     ht[k] = 'ok'
        #     return f(nd.next)
        # res = f(head)
        i = 0
        l = 10**4
        c = head
        while c:
            if not c.next:
                return False
            c = c.next
            i += 1
            if i > l:
                return True


        return res
    

head = [3,2,0,-4]
pos = 1
#
# head = [-21,10,17,8,4,26,5,35,33,-7,-16,27,-12,6,29,-12,5,9,20,14,14,2,13,-24,21,23,-21,5]
# pos = -1
head = create_linked_list(head, pos)
print(Solution().hasCycle(head))

        