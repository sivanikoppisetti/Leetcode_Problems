class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Prefix + Hashmap Solution
        csum = 0 # This is our prefix sum
        d = {0:1} # How many subarrays have we seen with sum k
        subarray_count = 0 # How many subarrays have we seen with sum k

        for right in range(len(nums)):
            # Compute prefix sum
            csum += nums[right]
            # Required prefix sum (prefix(l-1),history)
            req = csum - k 
            # check if req in d prefixes so far
            if req in d:
                subarray_count += d[req] #add the number of times we seen that prefix
            # push the current prefix in hashmap
            d[csum] = d.get(csum,0) + 1
        return subarray_count
            
        