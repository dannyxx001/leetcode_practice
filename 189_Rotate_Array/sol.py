class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        #nums = [1,2,3,4,5,6,7]
        #k = 3
        pos = len(nums) - k % len(nums)
        nums.extend(nums[:pos:])
        del nums[:pos:]
