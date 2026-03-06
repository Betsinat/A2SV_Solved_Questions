class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:  
                break
        else:
            return None  
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow  
