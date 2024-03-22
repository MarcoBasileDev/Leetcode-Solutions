class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        # Find the middle node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Reverse the second half
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        
        # Compare val of the first half and the second half
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            
            left = left.next
            right = right.next
            
        return True

        # Time Complexity O(n)
        # Space Complexity O(1)