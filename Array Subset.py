
from collections import Counter
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
      freq_a = Counter(a)
      freq_b = Counter(b)
      for key in freq_b:
          if freq_b[key] > freq_a[key]:
              return False
      return True
        
    
    
    
    
