class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left,right = 1,max(piles)
        ans=0
        while left<=right:
            k = (left+right)//2

            hours = 0
            for p in piles:
                hours+=(k+p-1)//k
            
            if hours<=h:
                ans=k
                right = k-1
            else:
                left=k+1
        return ans