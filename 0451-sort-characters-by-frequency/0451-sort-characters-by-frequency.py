class Solution:
    def frequencySort(self, s: str) -> str:
        ans = ""
        count = Counter(s)
        sorted_by_count = sorted(count.items(), key=lambda x: (-x[1], x[0]))
        for k ,v in  sorted_by_count:
            ans += k*v
        return ans
        