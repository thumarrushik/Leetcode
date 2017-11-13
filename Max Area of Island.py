class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        if grid is None:
            return 0
        
        m = len(grid)
        n = len(grid[0])
        
        def areas(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                grid[i][j] = 0
                return 1+areas(i-1,j) + areas(i+1,j) + areas(i,j-1) + areas(i,j+1)
            return 0
    
    
    
        maximum = 0
        
        for a1 in range(m):
            for b1 in range(n):
                if grid[a1][b1] == 1:
                    maximum = max(maximum, areas(a1,b1))
                    
        return maximum
        
        
    
            
