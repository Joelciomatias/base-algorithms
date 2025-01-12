# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1

        while list1 or list2:

            val1 = list1.val
            val2 = list2.val
            if not val1 and not val2:
                return list1
            
            if val1 and val1 <= (val2 or 0):
                list1.next = list2 
            else:
                next_node = list1.next
                list1.next = list2
                list2.next = next_node


        return list1
    
# Reverse the linked list
solution = Solution()
reversed_head = solution.mergeTwoLists(head)