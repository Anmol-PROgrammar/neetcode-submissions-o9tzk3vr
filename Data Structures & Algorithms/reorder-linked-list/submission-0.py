# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # cal length
        length = 0
        start = tail = head
        while tail:
            length += 1
            tail = tail.next

        n = length - length // 2 - 1
        
        # Loop and reorder
        # Repeat
        for i in range(n):
            tail = start
            # iterate to 2 element
            # store the last element and break the condition
            while tail.next.next:
                tail = tail.next

            # store last element
            lastNode = tail.next
            # break the link with last element to avoid cycle
            tail.next = None

            tmp = head.next
            head.next = lastNode
            lastNode.next = tmp
            head = tmp
