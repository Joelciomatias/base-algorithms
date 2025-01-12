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
        n1=list1
        n2=list2
        res = None
        if list1.val >= list2.val:
            res = list2
            n2 = n2.next
        else: 
            res = list1
            n1 = n1.next
        r = res

        while n1 and n2:
            if n1.val >= n2.val:
                r.next = n2
                n2 = n2.next
            else:
                r.next = n1
                n1 = n1.next
            r = r.next
        if n2:
            r.next = n2
        elif n1:
            r.next = n1

        return res


# Test the code with input [1, 2, 3, 4, 5]
# list1 = [1,2,4]
# list2 = [1,3,4]

list1 = [2]
list2 = [1]
head = create_linked_list(list1)
head2 = create_linked_list(list2)
# Reverse the linked list
solution = Solution()
reversed_head = solution.mergeTwoLists(head,head2)