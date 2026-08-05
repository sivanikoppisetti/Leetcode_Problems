class Solution:
    def maxPower(self, s: str) -> int:
        count = 1
        maxcount = 1
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                count += 1
            else:
                if count > maxcount:
                    maxcount = count
                count = 1
        return max(maxcount,count)


        