# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        values = []
        for node in lists:
            while node:
                values.append(node.val)
                node = node.next
        values.sort()
        dummy = ListNode()
        curr = None
        for val in values:
            node = ListNode(val) 
            if dummy.next is None:
                dummy.next = node
                curr = node
            if curr:
                curr.next = node
                curr = curr.next
        return dummy.next
