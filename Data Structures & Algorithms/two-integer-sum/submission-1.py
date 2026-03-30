class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        copy = {}
        complement = 0

        for i,n in enumerate(nums):
            complement = target-n
            if complement in copy:
                return [copy[complement],i]
            copy[n]=i
        return []