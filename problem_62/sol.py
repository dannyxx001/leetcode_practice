class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m > n:
            m,n = n,m
        paths = [[0 for j in xrange(n)] for i in xrange(m)]
        for i in xrange(m):
            for j in xrange(i,n):
                if i == 0:
                    paths[i][j] = 1
                elif i == j:
                    paths[i][j] = paths[i-1][j] * 2
                else:
                    paths[i][j] = paths[i-1][j] + paths[i][j-1]
        
        #print paths
        
        return paths[m-1][n-1]