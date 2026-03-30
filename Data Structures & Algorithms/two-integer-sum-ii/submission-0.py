class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left =0
        right =len(numbers)-1
        total = numbers[right]+numbers[left]

        while right>left:
            if total == target:
                return [left+1,right+1]
            elif total<target:
                left+=1
                total = numbers[right]+numbers[left]
            elif total>target:
                right-=1
                total = numbers[right]+numbers[left]
        return []