class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        dict = {}
        for i in nums:
            if i in dict:
                count += dict[i]
                dict[i] += 1
            else:
                dict[i] = 1
        return count
            
        
    
"""" class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if (nums[i] == nums[j]) & (i<j):
                    count +=1
        return count"""
        