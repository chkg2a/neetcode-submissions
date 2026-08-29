# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        bro = dummy
        curr = head
        while n > 0 and curr:
            curr = curr.next
            n-=1

        while curr and bro:
            bro = bro.next 
            curr = curr.next

        if bro and bro.next: 
            bro.next = bro.next.next
        
        return dummy.next