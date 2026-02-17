class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        res = []
        n = len(changed)
        if n % 2 != 0:
            return []
      
        changed.sort()
        cnt = Counter(changed)
        for x in changed:
            if cnt[x] == 0:
                continue
            if cnt[2*x] == 0:
                return []
            cnt[x] -= 1
            cnt[2*x] -=1
            res.append(x)           
        return res

        
        