class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = Counter(s)
        count_t = Counter(t)
        res = 0
        for k , v in count_s.items():
            if count_t[k] < count_s[k]:
                res += abs(count_t[k] - count_s[k])
        return res


       

        