class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result =[]
        path =[]

        def dfs(i,remain):
            if remain ==0:
                result.append(path.copy())
                return
            
            if i==len(nums) or remain<0:
                return
            
            # taking current candidates
            path.append(nums[i])
            dfs(i,remain-nums[i])
            path.pop()

            #skip current candidate
            dfs(i+1,remain)

        dfs(0,target)

        return result