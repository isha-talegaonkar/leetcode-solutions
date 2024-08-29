class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x<0 else 1
        number = abs(x)
        res = 0
        
        while number:
            number, remainder = divmod(number, 10)
            # remainder = number % 10
            # number /= 10
            res = res * 10 + remainder
            if res > 2**31 -1:
                return 0
        
        return res * sign