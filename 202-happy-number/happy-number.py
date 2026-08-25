def get_d_sum(num):
    
    d_sum = 0
    while num>0:
        r = num%10
        d_sum += r*r
        num = num//10
    return d_sum

class Solution:
    def isHappy(self, n: int) -> bool:
        
        while True:
            if n < 10:
                break
            n = get_d_sum(n)

        if n == 1 or n == 7:
            return True
        else:
            return False
    