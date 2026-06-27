# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while slow and fast.next:
            fast = fast.next
            if slow == fast:
                return True
            slow = slow.next
            if fast.next:
                fast = fast.next
            else:
                return False
        return False
