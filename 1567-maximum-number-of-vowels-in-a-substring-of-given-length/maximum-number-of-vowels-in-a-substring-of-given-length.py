class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left = 0
        Max_vowel_count = 0
        count = 0
        for right in range(len(s)):
            if s[right] in "aeiou":
                count += 1
            if right >= k-1:
                Max_vowel_count = max(Max_vowel_count,count)
                if s[left] in "aeiou":
                    count -= 1
                left += 1
        return Max_vowel_count
                
        