class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        self.dfs(0,[],nums,result)
        return result

    def dfs(self,index,subset,nums,result):
        result.append(subset)
        for i in xrange(index,len(nums)):
            if(i != index and nums[i] == nums[i-1]):
                continue
        self.dfs(i+1,subset+[nums[i]],nums,result)
