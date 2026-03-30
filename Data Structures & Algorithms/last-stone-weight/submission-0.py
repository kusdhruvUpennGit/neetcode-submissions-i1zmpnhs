class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            stone1 = -heapq.heappop(maxHeap) #largest
            stone2 = -heapq.heappop(maxHeap) #second largest

            if stone1 != stone2:
                heapq.heappush(maxHeap, -(stone1-stone2))
        
        return -maxHeap[0] if maxHeap else 0