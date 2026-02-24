class Solution(object):
    def canConstruct(self, ransomNote, magazine):
      a = Counter(ransomNote)
      b = Counter(magazine)
      for  char in ransomNote:
        if a[char] > b[char]:
            return False
      return True