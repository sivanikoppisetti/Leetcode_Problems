class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        Max_average = -10000000
        left = 0
        current_sum = 0
        for right in range(len(nums)):
            current_sum += nums[right]
            if right >= k-1:
                avg = current_sum / k
                Max_average = max(avg,Max_average)
                current_sum -= nums[left]
                left += 1
        return Max_average
        