# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head:
            return

        size = 0
        tail = head
        while tail:
            tail = tail.next
            size += 1

        if size == n:
            return head.next

        counter = 0
        nodeToPop = head
        while counter < size - n:
            nodeToPop = nodeToPop.next
            counter+=1
        tail = head
        while nodeToPop != tail.next:
            tail = tail.next
        tail.next = tail.next.next

        return head
        












