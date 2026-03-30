class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW=len(matrix)
        COL = len(matrix[0])

        top=0
        bot = ROW-1

        while top<=bot:
            row = (top+bot)//2

            if target>matrix[row][-1]:
                top=row+1
            elif target<matrix[row][0]:
                bot=row-1
            else:
                break
        
        if not (top<=bot):
            return False
        
        row = (top+bot)//2

        l=0
        r=COL-1

        while r>=l:
            middle=(r+l)//2
            if target>matrix[row][middle]:
                l=middle+1
            elif target<matrix[row][middle]:
                r=middle-1
            else:
                return True
        return False

