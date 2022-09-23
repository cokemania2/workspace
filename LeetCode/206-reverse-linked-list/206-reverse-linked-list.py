# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverse_node(head) 
        
    def reverse_node(self, node, prev=None):
        if node is None:
            return prev
        n = node.next
        node.next = prev
        return self.reverse_node(n, node)
