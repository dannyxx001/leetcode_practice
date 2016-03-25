class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        """
        nums = [1,3,5,6]
        target = 5
        """
        for i in xrange(len(nums)):
            if nums[i] < target:
                continue
            else:
                return i
        return len(nums)
