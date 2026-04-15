class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=right=0
        seen = set()
        maxLength=0
        while right<len(s):
            if s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            right+=1
            length = right-left+1
            maxLength = max(length,maxLength)
        return maxLength