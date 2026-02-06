class Solution:    
    def findUnion(self, a, b):
      union=list(set(a) | set(b))
      return union
