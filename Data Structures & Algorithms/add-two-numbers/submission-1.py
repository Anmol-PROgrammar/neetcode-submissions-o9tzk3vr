# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = tail = ListNode(0)
        carry = 0
        while l1 and l2:
            sum = l1.val + l2.val + carry
            carry = 0
            if sum >= 10:
                carry = (sum - (sum % 10)) // 10
                sum %= 10
                # print(carry, " ", sum)
            tail.next = ListNode(sum)
            tail = tail.next
            l1 = l1.next
            l2 = l2.next

        remain = l1 or l2
        while remain:
            sum = remain.val + carry
            carry = 0
            if sum >= 10:
                carry = (sum - sum % 10) // 10
                sum %= 10
                # print(carry, " ", sum)
            tail.next = ListNode(sum)
            tail = tail.next
            remain = remain.next

        if carry > 0:
            tail.next = ListNode(carry)

        return ans.next
















