class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        return [sorted_nums.index(i) for i in nums ]
    
    
    """class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        cp = sorted(nums)
        ret = []
        for i in nums:
            ret.append(cp.index(i))
        return ret
        """
        