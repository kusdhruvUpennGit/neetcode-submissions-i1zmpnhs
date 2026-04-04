class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = [1]*len(nums)

        prefix = 1
        for i in range(len(nums)):
            result=prefix
            prefix*=nums[i]
        
        suffix = 1
        for i in range(len(nums)-1,-1,-1):
            result *=suffix
            suffix*=nums[i]
        return result
