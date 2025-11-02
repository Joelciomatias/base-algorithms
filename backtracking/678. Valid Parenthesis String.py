from functools import lru_cache

class Solution:

    def checkValidString(self, s: str) -> bool:
        @lru_cache(maxsize=None)
        def valid(i=0, left=0):
            print()
            if left < 0:
                return False
            if i == len(s):
                return left == 0
            
            if s[i] == '(':
                return valid(i + 1, left + 1)
            elif s[i] == ')':
                return valid(i + 1, left - 1)
            elif s[i] == '*':
                return (
                    valid(i + 1, left + 1) or  # trata '*' como '('
                    valid(i + 1, left - 1) or  # trata '*' como ')'
                    valid(i + 1, left)         # trata '*' como ''
                )
            else:
                return False

        return valid()


s = "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"

print(Solution().checkValidString(s))