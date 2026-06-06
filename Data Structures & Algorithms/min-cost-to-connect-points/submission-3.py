class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        min_dist = [float("inf")]*n
        min_dist[0]=0

        in_mst = [False]*n

        total_cost = 0

        for _ in range(n):
            curr = -1
            for i in range(n):
                if not in_mst[i] and (curr==-1 or min_dist[i]<min_dist[curr]):
                    curr=i
            in_mst[curr]=True
            total_cost+=min_dist[curr]

            x1,y1 = points[curr]

            for next_point in range(n):
                if not in_mst[next_point]:
                    x2,y2 = points[next_point]
                    cost = abs(x1-x2)+ abs(y1-y2)
                    if cost<min_dist[next_point]==cost:
                        min_dist[next_point]=cost
        return cost