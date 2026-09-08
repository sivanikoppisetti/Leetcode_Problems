class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        previous = 0
        current = 0
        for i in range(len(nums)):
            if nums[i] in d.keys():
                previous = d[nums[i]]
                current = i
                if abs(previous-current) <= k:
                    return True
                else:
                    d[nums[i]] = i
            else:
                d[nums[i]] = i
        return False
        