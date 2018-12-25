import string

class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        def matches(s1map, s2map):
            for c in string.ascii_lowercase: # a-z
                if s1map[c] != s2map[c]:
                    return False
            return True
        
        # Sliding window method
        if len(s1) > len(s2):
            return False
        
        s1map = {}
        s2map = {}
        for c in string.ascii_lowercase: # a-z
            s1map[c] = 0
            s2map[c] = 0
        for i in range(len(s1)):
            s1map[s1[i]] += 1
            s2map[s2[i]] += 1  
        
        for i in range(len(s2) - len(s1)):
            if matches(s1map, s2map):
                return True
            s2map[s2[i+len(s1)]] += 1
            s2map[s2[i]] -= 1
        return matches(s1map, s2map)
