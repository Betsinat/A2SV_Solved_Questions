class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        update = [set(arr) for arr in responses]
        res = Counter(w for word in update for w in word) 
        max_count = -1
        max_word = ""
        for k , v in res.items():
            if v > max_count or (v == max_count and k < max_word):
                max_word = k
                max_count = v
        return max_word


       
        


        