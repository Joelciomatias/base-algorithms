class Solution:
    def isValid(self, s: str) -> bool:

        opened = {'{':1,"[":1,"(":1}
        c = {']':'[',')':'(','}':'{'}

        if len(s) % 2 != 0:
            return False

        stack = []
        for i in s:
            if opened.get(i):
                stack.append(i)
            elif stack:
                if stack.pop() != c[i]:
                    return False
            else:
                return False

        return not stack
