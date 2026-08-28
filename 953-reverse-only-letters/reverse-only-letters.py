class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        left = 0
        right = len(s)-1
        lst = list(s)
        while left < right:
                if lst[left].isalpha() and lst[right].isalpha():
                    lst[left],lst[right] = lst[right],lst[left]
                    left+= 1
                    right-=1
                elif lst[left].isalpha():
                    right -= 1
                elif lst[right].isalpha():
                    left += 1
                else:
                    left += 1
                    right -= 1
        result = ''.join(lst)
        return result


        
        