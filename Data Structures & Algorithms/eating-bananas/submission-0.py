class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Search space for k (bananas/hour)
        left, right = 1, max(piles)
        ans = right

        while left <= right:
            k = (left + right) // 2

            # Compute hours needed if Koko eats at speed k
            hours = 0
            for p in piles:
                # ceil(p / k) without using math.ceil
                hours += (p + k - 1) // k

            # If she can finish within h hours, k is valid -> try smaller k
            if hours <= h:
                ans = k
                right = k - 1
            else:
                # Too slow -> need bigger k
                left = k + 1

        return ans