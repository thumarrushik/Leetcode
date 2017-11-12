class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if height is None and len(height) == 0:
            return height
        
        low= 0
        high = len(height)-1
        maximum = 0
        
        
        while low < high:
            maximum = max(maximum, (high-low)*min(height[low], height[high]))
            
            if height[low] < height[high]:
                low += 1
            else:
                high -= 1
            
        return maximum
