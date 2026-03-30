class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        count={}
        for n in s:
            count[n]=count.get(n,0)+1
        
        for n in t:
            if n not in count:
                return False
            count[n]-=1
        
        for n in s:
            if count[n]<0:
                return False
        return True