class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Brute force
        '''
        res = 0
        for l in range(len(heights)):
            for r in range(l+1,len(heights)):
                area = (r-l) * min(heights[l],heights[r])
                res = max(res,area)
        return res
        '''
        
        # Two pointer method
        left = 0
        right = len(heights)-1
        max_area = 0
        while left<right:
            area = (right-left)*(min(heights[left],heights[right]))
            max_area = max(max_area,area)
            if heights[right]>heights[left]:
                left+=1
            else:
                right-=1
        return max_area