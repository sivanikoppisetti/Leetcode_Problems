class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        square = []
        for i in nums:
            value = i * i
            square.append(value)
        return sorted(square)

        