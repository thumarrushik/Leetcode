class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums is None and len(nums) == 0:
            return nums
        
        Result = [0]*len(nums)
        temp = 1
        
        for a1 in range(len(nums)):
            Result[a1] = temp
            temp *=nums[a1]
            
        temp = 1
        for b1 in range(len(nums)-1,-1,-1):
            Result[b1] *= temp
            temp *= nums[b1]
            
        return Result
            
