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
      
      
"""class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        def mergeSort(array):
            if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
                r = len(array)//2
                L = array[:r]
                M = array[r:]

        # Sort the two halves
                mergeSort(L)
                mergeSort(M)

                i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
                while i < len(L) and j < len(M):
                    if L[i] < M[j]:
                        array[k] = L[i]
                        i += 1
                    else:
                        array[k] = M[j]
                        j += 1
                    k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
                while i < len(L):
                    array[k] = L[i]
                    i += 1
                    k += 1

                while j < len(M):
                    array[k] = M[j]
                    j += 1
                    k += 1
        mergeSort(nums)"""
