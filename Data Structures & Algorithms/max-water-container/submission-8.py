class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        left = 0
        right = len(heights)-1
        maxArea = 0
        while left<right:
            area = (right-left)*min(heights[right],heights[left])
            maxArea = max(area,maxArea)
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return maxArea