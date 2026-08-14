class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sum = [0]
        add = 0
        for i in range(len(nums)):
            add += nums[i]
            prefix_sum.append(add)
        
        for i in range(len(nums)):
            leftsum = prefix_sum[i]
            rightsum = prefix_sum[len(nums)]-prefix_sum[i+1]
            if leftsum == rightsum:
                return i
        return -1


        