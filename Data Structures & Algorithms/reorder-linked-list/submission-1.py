# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        mid = fast = head
        # find mid
        while fast and fast.next:
            mid = mid.next
            fast = fast.next.next

        # reverse the elements from mid
        secondList = mid.next
        mid.next = prev = None
        mid = secondList

        while mid:
            tmp = mid.next
            mid.next = prev
            prev = mid
            mid = tmp

        while prev and head:
            tmp = head.next
            tmp2 = prev.next    
            head.next = prev
            prev.next = tmp
            head = tmp
            prev = tmp2

            




