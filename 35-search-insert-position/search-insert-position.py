class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
        nums.append(target) 
        new_arr = sorted(nums)
        index = 0
        for i in range(len(new_arr)):
            if new_arr[i] == target:
                index = i
        return index
        