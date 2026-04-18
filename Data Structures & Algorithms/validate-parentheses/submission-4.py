class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')':'(',
            '}':'{',
            ']':'['}
        
        for c in s:
            if c in pair:
                if stack[c] and stack[-1] == pairs[c]:
                    stack.pop()
                else:
                    return False
                stack.append(c)
        if stack ==[]:
            return True
        else:
            return False