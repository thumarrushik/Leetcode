class Solution:
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        la = len(A)
        lb = len(B)
        
        result = {}
        
        for a1, b1 in enumerate(B):
            if b1 not in result:
                result[b1] = []
            result[b1].append(a1)
            
        return [result[a2].pop() for a2 in A]
