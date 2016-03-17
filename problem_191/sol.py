class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # too slow
        """
        sum = 0
        for num in bin(n)[2::]:
            sum += int(num)
        return sum
        """
        # a little slow
        return bin(n).count('1')
