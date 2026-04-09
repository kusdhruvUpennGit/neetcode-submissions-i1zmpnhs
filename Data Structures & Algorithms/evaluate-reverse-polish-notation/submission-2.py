class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = []
        for token in tokens:
            if token == "+":
                b = result.pop()
                a = result.pop()
                result.append(a+b)
            elif token == "*":
                b = result.pop()
                a = result.pop()
                result.append(a*b)
            elif token == "/":
                b = result.pop()
                a = result.pop()
                result.append(int(a/b))
            elif token == "-":
                b = result.pop()
                a = result.pop()
                result.append(a-b)
            else:
                result.append(int(token))
        return result