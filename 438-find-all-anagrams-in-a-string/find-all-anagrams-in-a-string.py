class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #step-1: compute  the frequenices of string p
        d1 = {}
        for i in p:
            d1[i] = d1.get(i,0) + 1
        #step - 2: dO a k-length sliding window on s
        #Count the frequencies of characters in substring into d1
        
        lst = []
        d2 = {}
        left = 0
        for right in range(len(s)):
            d2[s[right]] = d2.get(s[right],0) + 1 
            # Counting freq of substring k
            if right >= len(p)-1:
            # checking the validity of window
                if d1 == d2: 
                # comparsion haspmap to check anagrams
                  lst.append(left) 
                # if anagrams adding start index to lst

                # Removing the outgoing element left
                d2[s[left]] -= 1
                if d2[s[left]] == 0:
                     d2.pop(s[left])
                left += 1
        return lst
            
            
        