class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        #s1 = "ab"
        #s2 = "ba"
        if(len(s1) != 1 or len(s2) != 1):
            pass
        elif(len(s1) != len(s2)):
            return False
        elif(s1 == s2):
            return True
        elif(len(s1) == 1):
            return False
        
        for i in xrange(len(s1)):
            if(i > 0 and i < len(s1) and self.isScramble(s1[:i:],s2[:i:]) and self.isScramble(s1[i::],s2[i::])):
                print s1[:i:],s1[i::]
                return True
            if(i > 0 and i < len(s1) and self.isScramble(s1[i::],s2[:i:]) and self.isScramble(s1[:i:],s2[i::])):
                return True
