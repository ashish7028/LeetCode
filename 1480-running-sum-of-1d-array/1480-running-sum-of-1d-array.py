class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        temp = []
        a= 0
        for i in range(len(nums)):
            a = a + nums[i]
            temp.append(a)
        return temp