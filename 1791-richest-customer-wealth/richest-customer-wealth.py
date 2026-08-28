class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sum1 = 0
        result = []
        for row in accounts:
            sum1 = 0
            for i in row:
                sum1 += i
            result.append(sum1)
        return max(result)
        