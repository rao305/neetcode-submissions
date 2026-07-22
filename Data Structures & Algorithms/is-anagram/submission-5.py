class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        from collections import Counter

        freq = Counter(s)
        freq = Counter(t)

        if Counter(s) == Counter(t):
            return True
        else:
            return False

        
        