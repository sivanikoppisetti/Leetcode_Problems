class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeroscount = 0
        maxlength = 0
        left = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeroscount += 1
            #Find invalid state, until valid shrink()
            while zeroscount > k:
                # Shrink()
                if nums[left] == 0:
                    zeroscount -= 1
                left += 1
            # Update max length
            maxlength = max(maxlength,right-left+1)
        return maxlength
        