class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = Counter(s)
        result = []
        for ch in order:
            if ch in freq:
                result.append(ch*freq[ch])
                del freq[ch]
        for ch in freq:
            result.append(ch*freq[ch])
        return "".join(result)