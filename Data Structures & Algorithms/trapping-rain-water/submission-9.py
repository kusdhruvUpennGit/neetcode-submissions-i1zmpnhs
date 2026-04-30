class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left = 0
        leftMax = height[left]
        right = len(height)-1
        rightMax = height[right]

        while left<right:
            if leftMax<rightMax:
                left+=1
                leftMax = max(leftMax,height[left])
                water+=leftMax-height[left]
            else:
                right-=1
                rightMax = max(rightMax,height[right])
                water+=rightMax-height[right]
        return water