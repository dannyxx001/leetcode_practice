class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        record = []
        while True:
            if n in record:
                return False
            
            record.append(n)
            
            tmp = 0
            while n > 0:
                tmp += (n % 10) ** 2
                n /= 10
            if tmp == 1:
                return True
            n = tmp
            