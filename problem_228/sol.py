class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        begin = ""
        end = ""
        sum_range = []
        for num in nums:
            if begin == "":
                begin = num
                tmp = num + 1
            elif tmp == num:
                end = num
                tmp += 1
            else:
                if end == "":
                    sum_range.append("%d" % begin)
                else:
                    sum_range.append("%d->%d" % (begin,end))
                begin = num
                tmp = num + 1
                end = ""
        if num == nums[len(nums)-1]:
            if end == "":
                sum_range.append("%d" % begin)
            else:
                sum_range.append("%d->%d" % (begin,end))
        return sum_range
