class Solution:
    def frequencySort(self, s: str) -> str:
        s_d = {}
        for i in s:
            if i in s_d:
                s_d[i] += 1
            else:
                s_d[i] = 1
        
        #res1 = sorted(s_d.items())
        res = sorted(s_d.items(), key=lambda x: x[1], reverse=True)
        
        ans = ""
        for char, freq in res:
            ans += char * freq
            
        return ans
    


        