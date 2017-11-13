class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        if grid is None or grid == []:
            return 0
        
        
        m = len(grid)
        n = len(grid[0])
        
        
        def merge(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == "1":
                grid[i][j] = "0"
                merge(i-1, j)
                merge(i+1, j)
                merge(i, j-1)
                merge(i, j+1)
                
                return 1
            return 0
        
        result = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    result += merge(i,j)
                    
        return result
