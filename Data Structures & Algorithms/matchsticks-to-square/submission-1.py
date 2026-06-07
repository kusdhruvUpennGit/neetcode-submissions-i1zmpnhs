class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if len(matchsticks)<4:
            return False
        total_length = sum(matchsticks)

        if total_length%4!=0:
            return False
        
        target = total_length//4

        matchsticks.sort(reverse=True)
        
        if matchsticks[0]>target:
            return False
        
        sides = [0,0,0,0]

        def backtrack(index):
            if index==len(matchsticks):
                return sides[0]==sides[1]==sides[2]==sides[3]==target
            current_stick = matchsticks[index]

            for side_index in range(4):
                if sides[side_index]+current_index>target:
                    continue
                
                if side_index>0 and sides[side_index]==sides[side_index-1]:
                    continue
                sides[side_index]+=current_stick

                if backtrack(index+1):
                    return True
                
                sides[side_index]-=current_stick
            return False
        return backtrack(0)