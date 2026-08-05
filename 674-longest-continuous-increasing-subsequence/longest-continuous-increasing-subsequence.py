class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        count = 1
        maxcount = 1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                count += 1
            else:
                if count > maxcount:
                    maxcount = count
                count = 1
        return max(maxcount,count)
        