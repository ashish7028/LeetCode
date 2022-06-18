class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = 0
        count = []
        for i in range(len(nums)):
            temp = 0
            for j in range(len(nums)):
                if (i != j) & (nums[j] < nums[i]) :
                    temp +=1
            count.append(temp)
        return count
        