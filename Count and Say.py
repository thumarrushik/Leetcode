class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        s = "1"
        
        for a1 in range(n-1):
            s = ''.join(str(len(list(group))) + digit for digit, group in itertools.groupby(s))
    
        return s
