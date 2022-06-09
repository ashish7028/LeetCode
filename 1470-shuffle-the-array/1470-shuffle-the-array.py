class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        temp = []
        for i,j in zip(nums[:n],nums[n:]):
            temp += [i,j]
        return temp
            
        