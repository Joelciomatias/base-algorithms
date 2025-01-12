class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        r = {}
        m = {}
        for c in magazine:
            m[c] = 1
        for c in ransomNote:
            m[c] = 1

        return False




s = Solution()
ransomNote, magazine =  "aa", "aab"

print(s.canConstruct(ransomNote, magazine))