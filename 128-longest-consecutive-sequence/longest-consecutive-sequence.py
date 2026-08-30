class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        count = 1
        maxcount = 1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1] and nums[i+1]-nums[i] == 1:
                count += 1
            elif nums[i+1] - nums[i] == 0:
                continue
            else: 
                if count > maxcount:
                    maxcount = count
                count = 1
        if len(nums) == 0:
            return 0    
        return max(maxcount,count)
            
    
        