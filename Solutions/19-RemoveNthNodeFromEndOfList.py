class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
            dummy = ListNode(0, head)
            slow = dummy
            fast = dummy

            # Move the fast pointer at n distance from the slow pointer
            while n > 0 and fast:
                fast = fast.next
                n -= 1

            # Move the slow pointer before the element that has to be removed
            while fast.next:
                slow = slow.next
                fast = fast.next
            
            # Delete the element
            slow.next = slow.next.next
            
            return dummy.next
    
    # Time Complexity O(n)
    # Space Complexity O(1)