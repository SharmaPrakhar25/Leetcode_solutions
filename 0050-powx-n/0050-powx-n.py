class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        if n < 0:
            x = 1/x
            n = -n
        
        halfPower = self.myPow(x, n//2)
        if n % 2 == 0:
            return halfPower * halfPower
        else:
            return halfPower * halfPower * x
        
        