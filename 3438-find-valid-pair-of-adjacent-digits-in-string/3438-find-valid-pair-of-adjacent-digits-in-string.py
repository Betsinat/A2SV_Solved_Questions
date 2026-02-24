class Solution:
    def findValidPair(self, s: str) -> str:
        count = Counter(s)
        for i in range(len(s) - 1):
            a, b = s[i], s[i + 1]
            if a != b and count[a] == int(a) and count[b] == int(b):
                return a + b 
        return ""  