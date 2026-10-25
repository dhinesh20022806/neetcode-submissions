# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        slow = fast = head

        count = n
        while count > 0 and fast:
            fast = fast.next
            
            count -= 1
        

        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = fast


        return head