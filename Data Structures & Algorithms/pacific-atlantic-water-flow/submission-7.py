class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
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
        
        #pacific (Top and LEft)
        for c in range(cols):
            dfs(0,c,pac,heights[0][c])
        for r in range(rows):
            dfs(r,0,pac,heights[r][0])
        
        #atlantic (bottom and right)

        for c in range(cols):
            dfs(rows - 1, c, atl, heights[rows - 1][c])
        for r in range(rows):
            dfs(r, cols - 1, atl, heights[r][cols - 1])

        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    result.append([r,c])
        return result