class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #nums = [2,13,-2,-5,-1,10,6,-8,5,-5,7,-5,-14,-4,-5,10,-15,-2,-14,-6,10,6,-14,-14,-9,-11,8,-3,-2,12,-9,-14,3,5,-12,-13,-8,1,-14,12,12,0,14,5,4,-14,-8,4,-9,-7,14,-13,6,7,-12,5,12,11,-13,-5,0,-6,-12,-12,6,13,12,13,0,5,2,-11,13,1,9,2,2,-14,13,8,-14,4,2,8,-3,-3,-10,-14,-15,14,-12,1,-15,14,-4,6,12,-6,-4,-3,6,5]
        nums.sort()
        sol_set = []
        i, j, k = 0, 0, 0
        while i < len(nums) and nums[i] <= 0 :
            j = i + 1
            k = len(nums)-1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == 0:
                    if [nums[i],nums[j],nums[k]] not in sol_set:
                        sol_set.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                elif sum < 0:
                    j += 1
                elif sum > 0:
                    k -= 1
            i += 1
        return sol_set
