class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in numSet:
            if n-1 not in numSet:
                start = n
                length = 1
                while start+1 in numSet:
                    start+=1
                    length+=1
                longest = max(length,longest)
        return longest