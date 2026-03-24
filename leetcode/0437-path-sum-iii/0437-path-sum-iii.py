class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        a = self.ps(root, targetSum)
        b = self.pathSum(root.left, targetSum)
        c = self.pathSum(root.right, targetSum)
        
        return a + b + c

    def ps(self, node, currentSum):
        if not node:
            return 0
        
        cnt = 0
        # Check if the current node's value matches the target
        if node.val == currentSum:
            cnt += 1
        
        # Continue the path downward with the remaining sum
        cnt += self.ps(node.left, currentSum - node.val)
        cnt += self.ps(node.right, currentSum - node.val)
        
        return cnt
        