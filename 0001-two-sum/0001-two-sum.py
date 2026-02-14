class Solution(object):
    def twoSum(self, nums, target):
        left, right = 0, len(nums) - 1
        # storing the individual element of the array with its index
        orginal_index = [(num, i) for i, num in enumerate(nums)]
        orginal_index.sort()
        arr = []
        while left < right:
            if orginal_index[left][0] + orginal_index[right][0] == target:
                arr.append(orginal_index[left][1])
                arr.append(orginal_index[right][1])
                break
            elif orginal_index[left][0] + orginal_index[right][0] < target:
                left += 1
            else:
                right -= 1
        return arr  