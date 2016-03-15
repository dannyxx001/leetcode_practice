class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True
        i = 0
        max_step = nums[0]
        while i <= max_step:
            if max_step >= len(nums)-1:
                return True
            if i+nums[i] > max_step:
                max_step = i+nums[i]
            i += 1
        return False
        
        # cost too much time
        """
        return self.canJumptoEnd(nums,0)
        
    def canJumptoEnd(self,nums,index):
        if index+nums[index] >= len(nums)-1:
            return True
        if nums[index] == 0 and index != len(nums)-1:
            return False
        for i in xrange(1,nums[index]+1):
            if self.canJumptoEnd(nums,index+i):
                return True
        return False
        """
