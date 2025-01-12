# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution class with recursive reverseList method
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def mf(node, prev):
            if not node:
                return prev
            next_node = node.next
            node.next = prev
            return mf(next_node, node)
        
        res = mf(head, None)
        return res

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

# Helper function to print a linked list
def print_linked_list(head):
    elements = []
    while head:
        elements.append(str(head.val))
        head = head.next
    print(" -> ".join(elements))

# Test the code with input [1, 2, 3, 4, 5]
input_list = [1, 2, 3, 4, 5]
head = create_linked_list(input_list)

print("Original Linked List:")
print_linked_list(head)

# Reverse the linked list
solution = Solution()
reversed_head = solution.reverseList(head)

print("Reversed Linked List:")
print_linked_list(reversed_head)
