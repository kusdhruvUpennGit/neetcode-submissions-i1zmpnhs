class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for n in numSet:
            if n-1 not in numSet:
                current = n
                length = 1
                while current+1 in numSet:
                    length+=1
                    current+=1
                longest = max(longest,length)
        return longest