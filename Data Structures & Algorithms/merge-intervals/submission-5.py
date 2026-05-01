class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        result = []
        intervals.sort(key=lambda x:x[0])
        result.append(intervals[0])

        for start,end in intervals[1:]:
            lastEnd = result[-1][1]
            if start<=lastEnd:
                result[-1][1] = max(lastEnd,end)
            else:
                result.append([start,end])
        return result