class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        new_list = []
        sum = 0
        for i in range(len(nums)):
             sum = sum + nums[i]
             new_list.append(sum)
        return new_list

        