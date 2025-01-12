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
    for val in elements[1:]:
        current.next = ListNode(val)
        current = current.next
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
    
# Helper function to create a linked list from a list
def create_linked_list(elements):
    if not elements:
        return None
    head = ListNode(elements[0])
    current = head
    for val in elements[1:]:
        current.next = ListNode(val)
        current = current.next
    return head
        