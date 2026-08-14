class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Compute prefix sum array
        prefix_sum = [0]
        sum1 = 0
        # runing sum
        for i in range(len(nums)):
             sum1 += nums[i]
             prefix_sum.append(sum1)
        
        #Find left sum and right sum for every index in nums
        for i in range(len(nums)):
            leftsum = prefix_sum[i]
            rightsum = prefix_sum[len(nums)]-prefix_sum[i+1]
            if leftsum == rightsum:
                return i
        return -1


        