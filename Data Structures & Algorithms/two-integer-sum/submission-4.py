class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = 0
        seen = [] # the hash table
        for i,n in enumerate(nums):
            complement = target - n
            if complement in seen:
                return [seen[complement],i] # returning the index
            seen[n] = i
        return []
