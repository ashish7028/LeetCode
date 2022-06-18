class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        d = {}
        snums = sorted(nums)
        for i,v in enumerate(snums):
            if v not in d:
                d[v]=i       
        return [ d[n] for n in nums ]
    
    
    """class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        cp = sorted(nums)
        ret = []
        for i in nums:
            ret.append(cp.index(i))
        return ret
        """
        