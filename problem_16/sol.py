from sys import maxint
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        N = len(nums)
        record = maxint
        i, j, k = 0, 0, 0
        while i < N-2:
            j = i+1
            k = N-1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if abs(sum-target) < abs(record-target):
                    record = sum
                if sum == target:
                    return target
                elif sum < target:
                    j += 1
                elif sum > target:
                    k -= 1
            i += 1
        return record
