class Solution:
    def climbStairs(self, n: int) -> int:
        sum =  [0] * (n + 1);
        if n == 1:
            return 1
        if n == 2:
            return 2
        sum[1] = 1
        sum[2] = 2
        for i in range(3,n+1):
            sum[i] = sum[i - 1] + sum[i - 2]
        return sum[n]
