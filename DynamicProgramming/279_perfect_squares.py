class Solution:
    def numSquares(self, n: int) -> int:
        
        memo = {}
    
        def numSquaresHelper(n, memo):
            if n == 0:
                return 0
            if n in memo:
                return memo[n]
            
            min_squares = float('inf')
            for i in range(1, int(math.sqrt(n)) + 1):
                square = i * i
                if square > n:
                    break
                min_squares = min(min_squares, 1 + numSquaresHelper(n - square, memo))
            
            memo[n] = min_squares
            return min_squares
        
        return numSquaresHelper(n, memo)
