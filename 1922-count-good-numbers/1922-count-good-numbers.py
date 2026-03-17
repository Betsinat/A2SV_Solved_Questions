class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        def pow_mod(x, n):
            res = 1
            while n > 0:
                if n % 2 == 1:
                    res = (res * x) % MOD
                x = (x * x) % MOD
                n //= 2
            return res

        even = (n + 1) // 2
        odd = n // 2

        return (pow_mod(5, even) * pow_mod(4, odd)) % MOD