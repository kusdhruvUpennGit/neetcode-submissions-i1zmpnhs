class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for c in nums:
            count[c]=count.get(c,0)+1
        
        minHeap = []

        for num,freq in count.items():
            heapq.heappush(minHeap,(freq,num))
            if len(minHeap)>k:
                heapq.heappop()
        return [num for freq,num in minHeap]