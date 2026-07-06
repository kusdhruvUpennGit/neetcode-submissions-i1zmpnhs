class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # This will store the bitwise OR of all elements.
        # Any bit that appears in at least one number can contribute to the final answer.
        total_or = 0

        # Build the OR of all numbers
        for num in nums:
            total_or |= num

        # If there are n numbers, there are 2^n subsets.
        # For every bit present in total_or, that bit appears in exactly half the subsets,
        # so multiply total_or by 2^(n - 1).
        return total_or * (1 << (len(nums) - 1))
