class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        r = {}
        m = {}
        for c in magazine:
            m[c] = m[c]+1 if m.get(c) else  1
        for c in ransomNote:
            r[c] = r[c]+1 if r.get(c) else  1

        for k in r:
            if not m.get(k) or m[k] < r[k]:
                return False

        return True




s = Solution()
ransomNote, magazine =  "aa", "aab"  # True
ransomNote, magazine = "aa", "ab" # False
ransomNote, magazine = "fihjjjjei", "hjibagacbhadfaefdjaeaebgi"

print(s.canConstruct(ransomNote, magazine))