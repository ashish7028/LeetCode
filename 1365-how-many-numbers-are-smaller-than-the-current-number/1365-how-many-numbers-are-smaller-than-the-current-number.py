class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        cp = sorted(nums)
        ret = []
        for i in nums:
            ret.append(cp.index(i))
        return ret
        