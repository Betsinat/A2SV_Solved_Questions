class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        left = 0
        right = (len(x)) - 1
        for _ in range(len(x)):
            if x[left] == x[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
