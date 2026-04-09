class Solution:
    def calculate(self, s: str) -> int:
        result = []
        num = 0
        sign = "+"

        for i in range(len(s)):
            char = s[i]
            if char.isdigit():
                num = num*10 + int(char)
            if char in "+-/*" or i==len(s)-1:
                if sign == "+":
                    result.append(num)
                elif sign == "-":
                    result.append(-num)
                elif sign == "*":
                    result.append(result.pop()*num)
                elif sign == "/":
                    result.append(int(result.pop()/num))
                
                sign = char
                num = 0
        return sum(result)