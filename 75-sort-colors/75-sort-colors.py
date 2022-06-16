class Solution:
    def sortColors(self, nums: List[int]) -> None:
        a = 0
        b= 0
        c= 0
        for i in nums:
            if i ==0:
                a +=1
            elif i==1:
                b  += 1
            else:
                c += 1
            for i in range(a):
                nums[i] = 0
            for j in range(b):
                nums[a+j] = 1
            for k in range(c):
                nums[a+b+k] = 2
      
      
        
        
