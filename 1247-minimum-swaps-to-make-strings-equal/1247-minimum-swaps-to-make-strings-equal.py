class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        count_xy = 0
        count_yx = 0
        for i in range(len(s1)):
            if s1[i] == 'x' and s2[i] == 'y':
                count_xy +=1
            elif s1[i] == 'y' and s2[i] == 'x':
                count_yx += 1
            
        if (count_xy + count_yx )% 2 != 0:
            return -1
        return((count_xy//2) + (count_yx//2) + (2 if count_xy%2 == 1 else 0))




