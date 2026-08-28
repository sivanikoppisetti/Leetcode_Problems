class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_d = {}
        for i in s:
            if i in s_d.keys():
                s_d[i] += 1
            else:
                s_d[i] = 1
        
        t_d = {}
        for j in t:
            if j in t_d.keys():
                t_d[j] += 1
            else:
                t_d[j] = 1
        
        for ch in t:
            if ch not in s:
                result = ch
            elif ch in s and s_d[ch] != t_d[ch]:
                result = ch *(abs(s_d[ch]-t_d[ch]))
        return result
        