class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        frequency = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n]=1 + count.get(n,0) # getting the number of occurences of n and adding it by 1 (default value is 0)
        
        for n,c in count.items():
            frequency[c].append(n) #this mentions that number n offurs c number of times in the array

        result=[]
        for i in range(len(frequency)-1,0,-1):
            for n in frequency[i]:
                result.append(n)
                if len(result)==k:
                    return result

        