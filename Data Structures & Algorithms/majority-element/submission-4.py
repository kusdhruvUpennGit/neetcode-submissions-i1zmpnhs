class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        maxCount = 0
        res = 0

        for num in nums:
            count[num] = 1 + count.get(num,0)
            if count[num]>maxCount:
                res = count[num]
            maxCount = max(count[num],maxCount)
        return res