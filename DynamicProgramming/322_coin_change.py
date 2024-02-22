class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = {}

        def dpcoin(coins, n, memo):
            if n == 0:
                return 0
            if n in memo:
                return memo[n]

            minCount = float('inf')
            for coin in coins:
                if coin <= n:
                    count = 1 + dpcoin(coins, n - coin, memo)
                    if count != 0:  # check if valid combination exists
                        minCount = min(minCount, count)

            memo[n] = minCount if minCount != float('inf') else -1
            return memo[n]

        return dpcoin(coins, amount, memo)
                
        
