class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        seen = set()
        maxLength=0
        for right in range(len(s)):
            if s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            length = right-left+1
            maxLength = max(length,maxLength)
        return maxLength