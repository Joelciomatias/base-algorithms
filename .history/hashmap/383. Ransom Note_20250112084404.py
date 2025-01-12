class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        r = {}
        m = {}
        for c in magazine:
            m[c] = 1
        for c in ransomNote:
            r[c] = 0

        for k in r:
            if not m.get(k):
                return False

        return True




s = Solution()
ransomNote, magazine =  "aa", "aab"  # True

print(s.canConstruct(ransomNote, magazine))