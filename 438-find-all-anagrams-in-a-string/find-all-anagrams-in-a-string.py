class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        d1 = {}
        for i in p:
            d1[i] = d1.get(i,0) + 1
        
        lst = []
        d2 = {}
        left = 0
        for right in range(len(s)):
            d2[s[right]] = d2.get(s[right],0) + 1
            if right >= len(p)-1:
                if d1 == d2:
                  lst.append(left)
                d2[s[left]] -= 1
                if d2[s[left]] == 0:
                     d2.pop(s[left])
                left += 1
        return lst
            
            
        