class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n!=1:
            if n in seen:
                return False
            seen.add(n)

            total = 0
            temp = n

            while temp:
                digit = temp%10
                total += (digit*digit)
                temp=temp//10
            
            n= total            
        return True