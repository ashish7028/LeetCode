"""class Solution:    
    def createTargetArray(self, nums: List[int], ind: List[int]) -> List[int]:
        lst = []
        for i in range(len(nums)):
            lst.insert(ind[i], nums[i])
        return lst"""




class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i ,j in zip(nums,index):
            target.insert(j,i)
        return target
            
            
        