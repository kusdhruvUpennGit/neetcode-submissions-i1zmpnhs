class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1

        while right>left:
            mid = (left+right)//2

            if nums[mid]>=nums[right]:
                # Minimum in right side
                left=mid+1
            else:
                right = mid
        return nums[left]