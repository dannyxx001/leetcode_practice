class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in xrange(0,len(nums),3):
            if nums[i] == nums[-1]:
                return nums[i]
            elif nums[i] != nums[i+1]:
                return nums[i]
