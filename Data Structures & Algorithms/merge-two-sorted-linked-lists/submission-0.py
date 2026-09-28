# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        

        head = None
        res = None
        currOne = list1
        currTwo = list2

        while currOne and currTwo:
            if currTwo.val < currOne.val:
                if res is None:
                    res = currTwo
                    head = res
                else:
                    res.next = currTwo
                    res = res.next
                currTwo = currTwo.next
            else:
                if res is None:
                    head = res = currOne
                else:
                    res.next = currOne
                    res = res.next
                currOne = currOne.next
        
        if currOne:
            if head is None:
                head = currOne
            else:
                res.next = currOne

        if currTwo:
            if head is None:
                head = currTwo
            else:
                res.next = currTwo
        return head
                