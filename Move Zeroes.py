class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None and len(nums) < 2:
            return nums            
        
        
        low = 0
        high = 1
        
        
        while high < len(nums) and low < len(nums):
            
            if nums[low] == 0 and nums[high] != 0:
                nums[low], nums[high] = nums[high], nums[low]
                
            if nums[low] != 0:
                low += 1
          
            high += 1
