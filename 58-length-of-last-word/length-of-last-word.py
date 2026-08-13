class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        result = words[-1]
        return len(result)
        