class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        for x,y in points:
            dist = (x*x) + (y*y)
            maxHeap.append((dist,x,y))
        
        heapq.heapify(maxHeap)

        res = []
        for _ in range(k):
            dist,x,y = heapq.heappop(maxHeap)
            res.append([x,y])
        
        return res