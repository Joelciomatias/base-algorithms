from collections import defaultdict

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
            else:
                stack.append([c,1])

            if stack[-1][1] == k:
                stack.pop()
            
        res = ''
        for char, count in stack:
            res += (char * count)
        return res


    def removeDuplicates2(self, s: str, k: int) -> str:
        st = []
        i = 0
        counter = defaultdict(int)
        while i < len(s):
            counter[s[i]] += 1
            st.append(s[i])

            if counter[s[i]] >= k:
                cc = 0
                for j in st[-k:]:
                    if j == s[i]:
                        cc +=1
                if cc == k:
                    st = st[:-k]
                    counter[s[i]] -= k
            i += 1
        return ''.join(st)
    
s = Solution()
print(s.removeDuplicates('yfttttfbbbbnnnnffbgffffgbbbbgssssgthyyyy', 4))
# print(s.removeDuplicates('pbbcggttciiippooaais',2))
