class Solution(object):
    def subsets(self, nums):
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
            self.dfs(i+1,subset+[nums[i]],nums,result)