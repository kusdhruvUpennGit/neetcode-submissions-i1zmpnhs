class Solution:
    def minOperations(self, s: str) -> int:
        alt1 = 0 # '0'
        alt2 = 0 # '1'

        for i,ch in enumerate(s):
            if ch != ('0' if i%2==0 else '1'):
                alt1+=1
            if ch != ('1' if i%2==0 else '0'):
                alt2+=1
        
        return min(alt1,alt2)