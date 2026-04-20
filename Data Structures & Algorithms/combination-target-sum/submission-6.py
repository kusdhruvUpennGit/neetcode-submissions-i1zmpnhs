class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        path = []
        def backtrack(i,remain):
            if i==len(nums) or remain<0:
                return
            if remain == 0:
                result.append(path.copy())
                return
            #taking current candidate
            path.append(nums[i])
            backtrack(i,remain-nums[i])
            path.pop()
            #skipping current candidate
            backtrack(i+1,remain)
        backtrack(0,target)
        return result