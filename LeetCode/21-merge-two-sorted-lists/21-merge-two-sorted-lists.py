# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def func(self, list1, list2, mergedList):
        if list1 is None and list2 is None:
            return
        if list1 is None:
            mergedList.next = list2
            return 
        if list2 is None:
            mergedList.next = list1
            return
            
        if list1.val < list2.val:
            mergedList.next = list1
            list1 = list1.next
        else:
            mergedList.next = list2
            list2 = list2.next
        self.func(list1, list2, mergedList.next)
        
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mergedList = ListNode()
        self.func(list1, list2, mergedList)
        return mergedList.next