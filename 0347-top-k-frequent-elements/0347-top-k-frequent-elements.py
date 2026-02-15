class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        n = len(nums)
        bucket = [[] for _ in range(n+1)]
        for num , count in freq.items():
            bucket[count].append(num)
        result = []
        for i in range(n ,  0 , -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result
            if len(result) == k:
                    break
