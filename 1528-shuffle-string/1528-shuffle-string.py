class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        d  = {}
        for i in range(len(indices)):
            d[indices[i]]=s[i]
        ans = ""
        for x in sorted(d):
            ans += d.get(x)
        return ans


        


          
    



        