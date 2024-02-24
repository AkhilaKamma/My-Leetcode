class Solution:

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        prices = [float('inf')] * n
        prices[src] = 0
       
        for i in range(k+1):
            tempPrices = prices.copy()

            for s,d,p in flights: #source,destintion,price
                
                if prices[s] == float('inf'): #This case arrises when the first tuple in the flights list is not a source node
                    continue
                
                if prices[s] + p < tempPrices[d]:
                    tempPrices[d] = prices[s] + p
            
            prices = tempPrices

        return -1 if prices[dst] == float('inf') else prices[dst]
                
                

