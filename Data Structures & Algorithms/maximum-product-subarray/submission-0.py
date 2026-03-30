class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = nums[0]
        curMin = nums[0]
        res = nums[0]

        for n in nums[1:]:
            candidates = (n,n*curMax,n*curMin)
            curMax = max(candidates)
            curMin = min(candidates)

            res = max(res,curMax)
        return res