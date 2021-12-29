# https://leetcode.com/problems/merge-two-sorted-lists/
# merge-two-sorted-lists.py

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        def get_next(l1, l2):
            if l1 == None and l2 == None:
                return (None, None, None)
            if l1 == None:
                return (l2, l1, l2.next)
            elif l2 == None:
                return (l1, l1.next, l2)
            elif l1.val < l2.val:
                return (l1, l1.next, l2)
            else:
                return (l2, l1, l2.next)
        
        def go_next(node, l1, l2):
            next_node, l1, l2 = get_next(l1, l2)
            if l1 is None and l2 is None:
                if node is not None:
                    node.next = next_node
                return node
            node.next = go_next(next_node, l1, l2)
            return node
        next_node, l1, l2 = get_next(list1, list2)
        return go_next(next_node,l1, l2)