class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        
        best = [0]*len(nums)
        best[0] = nums[0]
        best[1] = max(nums[0],nums[1])

        for i in range(2,len(nums)):
            best[i]= max(best[i-1],nums[i]+best[i-2])
        
        return best[-1]