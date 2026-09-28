# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if not head or not head.next or not head.next.next:
            return False
        
        slowPointer = head
        FastPointer = head.next.next

        while FastPointer and FastPointer.next:
            if slowPointer == FastPointer:
                return True
            slowPointer = slowPointer.next
            FastPointer = FastPointer.next.next
        return False