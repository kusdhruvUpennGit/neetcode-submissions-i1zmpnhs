class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        
        def robLine(houses):
            rob1,rob2=0,0
            for money in houses:
                newRob = max(rob1+money,rob2)
                rob1=rob2
                rob2=newRob

            return rob2
        
        return max(robLine(nums[:-1]),robLine(nums[1:]))