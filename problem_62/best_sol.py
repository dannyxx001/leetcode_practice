class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        """
        (m+n-2)!/((m-1)!(n-1)!)
        """
        return math.factorial(m+n-2)/(math.factorial(m-1)*math.factorial(n-1))
