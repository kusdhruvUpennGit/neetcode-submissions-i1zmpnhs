class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
        
        minHeap = [(0,k)] # (time, node)
        visited = set()
        t = 0

        while minHeap:
            time,node = heapq.heappop(minHeap)

            if node in visited:
                continue
            visited.add(node)
            t= time

            for nei,w in graph[node]:
                if nei not in visited:
                    heapq.heappush(minHeap, (time+w,nei))
        return t if len(visited) == n else -1