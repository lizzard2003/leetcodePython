# 905. Sort Array By Parity
#Given an interger array nums, move all the even intergers at the begining of the array
#followed by all the odd intergers
# Return any array that satisfies this condition
# This is a partitionong problem
# with a quick sort algorithm
# we use two pointers to solve

from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l=0
        for r in range(len(nums)):
            if nums[r]% 2== 0: # this is to see if the number is even 
                nums[l], nums[r]= nums[r], nums[l] # swap the numbers here to get the even to the left
                l +=1 # increase the l pointer by 1 to next number
        return nums
nums= [3,1,2,4]       
solution= Solution() 
sorted_nums= solution.sortArrayByParity(nums)
print(sorted_nums)
    
