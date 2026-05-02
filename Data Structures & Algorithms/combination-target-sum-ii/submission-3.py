class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        path = []

        def backtrack(start, path, target):
            if remain<0:
                return
            if remain ==0:
                result.append(path.copy())
                return
            
            for i in range(start,len(candidates)):
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                if candidates[i]>0:
                    break
                path.append(candidates[i])
                backtrack(i+1,path,remain-candidates[i])
                path.pop()
        backtrack(0,[],target)
        return result