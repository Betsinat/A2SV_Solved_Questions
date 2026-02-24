class Solution(object):
    def intersection(self, nums1, nums2):
       arr = []
       for num in nums1:
          if num in nums2:
            arr.append(num)
       a = set(arr)
       return list(a)