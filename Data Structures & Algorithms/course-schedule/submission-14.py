class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReq = {i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            preReq[crs].append(pre)
        visit=set()

        def dfs(crs):
            if crs in visit:
                return False
            if preReq[crs]==[]:
                return True
            visit.add(crs)
            for pre in preReq[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            preReq[crs]=[]
            return True
        for crs in numCourses:
            if not dfs(crs):
                return False
        return True