class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left = 0
        leftMax = height[left]
        right = len(height)
        rightMax = height(right)
        water=0
        while left<right:
            if height[left]<height[right]:
                left+=1
                leftMax = max(leftMax,height[left])
                water+= leftMax - height[left]
            else:
                right-=1
                rightMax = max(rightMax,height[right])
                water+= rightMax - height[right]
        return water