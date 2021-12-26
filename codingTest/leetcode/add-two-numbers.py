# https://leetcode.com/problems/add-two-numbers/submissions/
# add-two-numbers.py 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def extract_val(node):
            return node.val if node else 0
        
        def node_or_next(node):
            return node.next if node.next else ListNode()
        
        def make_node(l, l1, l2):
            val = l.val + extract_val(l1) + extract_val(l2)
            l.val = val % 10
            if l1.next == None and l2.next == None:
                if val // 10 > 0:
                    l.next = ListNode(val // 10)
                return l
            l.next = make_node(ListNode(val // 10),node_or_next(l1), node_or_next(l2))
            return l
        
        return make_node(ListNode(),l1, l2)