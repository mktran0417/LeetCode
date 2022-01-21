# Definition for singly-linked list.
from black import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        while l1.next:
            print(l1.val

obj = Solution()

obj.addTwoNumbers(ListNode([9, 9, 9, 9, 9, 9, 9]), [9, 9, 9, 9])
