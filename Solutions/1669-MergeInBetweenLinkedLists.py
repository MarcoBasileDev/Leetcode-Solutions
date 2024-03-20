# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        before_a = list1
        for _ in range(a - 1):
            before_a = before_a.next
        
        post_b = before_a.next
        for _ in range(b - a + 1):
            post_b = post_b.next

        before_a.next = list2
        while before_a.next:
            before_a = before_a.next

        before_a.next = post_b

        return list1

        # Time Complexity O(n)
        # Space Complexity O(1)