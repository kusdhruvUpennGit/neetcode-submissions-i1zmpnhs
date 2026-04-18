class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')':'(',
            '}':'{',
            ']':'['}
        
        for c in s:
            if c in pairs:
                if not stack and stack[-1] != pairs[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        if stack ==[]:
            return True
        else:
            return False