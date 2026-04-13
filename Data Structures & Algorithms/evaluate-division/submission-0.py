class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)

        for i, (a, b) in enumerate(equations):
            adj[a].append((b, values[i]))
            adj[b].append((a, 1 / values[i]))

        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1.0

            q = deque([(src, 1.0)])
            visit = set([src])

            while q:
                node, w = q.popleft()

                if node == target:
                    return w

                for nei, weight in adj[node]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append((nei, w * weight))

            return -1.0

        return [bfs(a, b) for a, b in queries]
