# Definition for singly-linked list.
from typing import Optional


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
            current = current.next
            i += 1


    return head


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
    

head = [3,2,0,-4]
pos = 1
head = create_linked_list(head, pos)

        