class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pac = set()
        atl = set()
        result = []

        def dfs(r,c,visit,prevHeight):
            if r<0 or c<0 or r>=rows or c>=cols or (r,c) in visit or heights[r][c]<prevHeight:
                return
            visit.add((r,c))
            dfs(r+1,c,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])
        #PACIFIC
        for r in range(rows):
            dfs(r,0,pac,heights[r][0])
        for c in range(cols):
            dfs(0,c,pac,heights[0][c])
        #ATLANTIC
        for r in range(rows):
            dfs(r,cols-1,atl,heights[r][cols-1])
        for c in range(cols):
            dfs(rows-1,c,atl,heights[rows-1][c])
        
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    result.append((r,c))
        return result