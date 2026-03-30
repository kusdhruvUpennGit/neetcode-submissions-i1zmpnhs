class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        parent = [i for i in range(N+1)]
        rank = [1]*(N+1)

        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        
        def union(a,b):
            rootA = find(a)
            rootB = find(b)

            if rootA==rootB:
                return False
            
            if rank[rootA]>rank[rootB]:
                parent[rootB]=rootA
            elif rank[rootB]>rank[rootA]:
                parent[rootA]=rootB
            else:
                parent[rootB]=rootA
                rank[rootA]+=1
            return True
        
        for u,v in edges:
            if not union(u,v):
                return [u,v]