import numpy as np
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums = np.array(nums)
        hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap.keys():
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i