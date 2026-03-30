class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left,right = 0,0
        longest = 0
        seen = set()
        length=0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])

            length = right-left+1

            if length>longest:
                longest=length

        return longest