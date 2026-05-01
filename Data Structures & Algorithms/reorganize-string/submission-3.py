class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = [(-freq,ch) for ch,freq in count.items()]
        heapq.heapify(maxHeap)
        result = []
        prevChar,prevCount = "",0

        while maxHeap:
            freq,ch = heapq.heappop(maxHeap)
            result.append(ch)
            if prevCount>0:
                heapq.heappush(maxHeap,(prevCount,prevChar))
            freq+=1
            prevCount,prevChar = freq,ch
        result = "".join(result)
        if len(s)==len(result):
            return result
        else:
            return ""