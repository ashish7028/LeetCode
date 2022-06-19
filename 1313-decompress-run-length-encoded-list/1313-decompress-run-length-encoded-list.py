class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        
        decode_output= []
        
		# linear scan with step size = +2
        for i in range( 0, len(nums), +2):
            
            frequency = nums[i]                             # get the frequency of token
            value     = nums[i+1]                           # get the value of token
            decode_output.extend( [value ] * frequency )    # decoding
            
            
        return decode_output