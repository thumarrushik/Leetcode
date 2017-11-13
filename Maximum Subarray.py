class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
        
        current = maximum = nums[0]
        for a1 in range(1,len(nums),1):
            current = max(nums[a1], current + nums[a1])
            
            if current > maximum:
                maximum = current
        return maximum
        
        
