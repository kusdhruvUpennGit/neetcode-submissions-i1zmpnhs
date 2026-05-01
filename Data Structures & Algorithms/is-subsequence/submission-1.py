class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        i = 0
        for j in range(len(t)):
            if s[i]==t[j]:
                i+=1
        if len(s)==i:
            return True
        else:
            return False