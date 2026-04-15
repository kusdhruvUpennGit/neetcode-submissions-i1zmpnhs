class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = []
        for i in operations:
            if i == "+":
                result.append(result[-1]+result[-2])
            elif i=="D":
                result.append(2*result[-1])
            elif i=="C":
                result.pop()
            else:
                result.append(int(i))
        return sum(result)