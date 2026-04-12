class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReq = {i:[] for i in range(numCourses)}

        for crs,pre in prerequisites:
            preReq[crs].append(pre)
        
        visited=set()

        def dfs(crs):
            if crs in visited:
                return False
            if preReq[crs]==[]:
                return True
            visited.add(crs)

            for pre in preReq[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            preReq[crs]=[]
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True