class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        path = []

        def dfs(i,remain):
            if i==len(nums) or remain<0:
                return 
            if remain == 0:
                result.append(path.copy())
                return
            # Choice of taking candidates
            path.append(nums[i])
            dfs(i,remain-nums[i])
            path.pop()
            # choice of skipping candidates
            dfs(i+1,remain)
        dfs(0,target)
        return result