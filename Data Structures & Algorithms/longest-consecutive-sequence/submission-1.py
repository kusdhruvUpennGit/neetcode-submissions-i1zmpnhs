class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        max_count = 0

        for n in numSet:
            if n-1 not in numSet:
                start = n
                count=1
                while start+1 in numSet:
                    start+=1
                    count+=1
                max_count = max(max_count,count)
        return max_count