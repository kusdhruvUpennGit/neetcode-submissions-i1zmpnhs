class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = []
        for i in range(operations):
            if operations[i] == "+":
                result.append(int(result[i-1])+int(result[i-2]))
            elif operations[i]=="D":
                result.append(2*int(result[i-1]))
            elif operations[i]=="C":
                result.pop()
            else:
                result.append(i)
        return result[0]