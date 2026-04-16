class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = [(-freq,ch) for ch,freq in count.items()]
        heapq.heapify(maxHeap)
        prevCount,prevChar = 0,""
        result = []

        while maxHeap:
            freq,ch =  heapq.heappop(maxHeap)
            result.append(ch)
            #put prevChar back if it still has remaining count
            if prevCount<0:
                heapq.heappush(maxHeap,(prevCount,prevChar))
            #current char used once, so increase freq towards 0
            freq+=1
            prevCount,prevChar = freq,ch
        
        result="".join(result)
        if len(s)==len(result):
            return result
        else:
            return ""