from math import log
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #n = 243
        """
        if n < 1:
            return False
        else:
            return abs(log(n,3) - round(log(n,3))) < 1e-10
        """
        return n >= 1 and abs(log(n,3) - round(log(n,3))) < 1e-10
