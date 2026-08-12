class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
      prefix_sum = []
      sum_ = 0
      for i in nums:
        sum_ += i
        prefix_sum.append(sum_)
      return prefix_sum
