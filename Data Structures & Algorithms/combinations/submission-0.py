class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        combination = []

        def backtrack(start):
            if len(combination)==k:
                result.append(combination[:])
                return
            
            for num in range(start, n+1):
                combination.append(num)
                backtrack(num+1)
                combination.pop()
        
        backtrack(1)
        return result