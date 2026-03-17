class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        curr = head
        while curr:
            while stack and curr.val > stack[-1]:
                stack.pop()
            stack.append(curr.val)
            curr = curr.next
        dummy = ListNode()
        curr = dummy
        for n in stack:
            curr.next = ListNode(n)
            curr = curr.next
        return dummy.next

       
        