class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        start = 0
        maxCount = 0
        count=0
        for n in numSet:
            if n-1 not in numSet:
                start = n
                count = 1
            while start+1 in numSet:
                start+=1
                count+=1
            maxCount = max(maxCount,count)
        return maxCount