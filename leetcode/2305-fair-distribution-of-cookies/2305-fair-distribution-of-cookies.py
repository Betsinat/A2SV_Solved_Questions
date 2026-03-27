class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        kids = [0] * k
        ans = float("inf")

        def back(i):
            nonlocal ans

            if i == len(cookies):
                unf = max(kids)
                ans = min(ans, unf)
                return
            
            for j in range(k):
                if kids[j] + cookies[i] > ans:
                    continue
                kids[j] += cookies[i]
                back(i + 1)
                kids[j] -= cookies[i]

                if kids[j] == 0:
                    break
        back(0)
        return ans