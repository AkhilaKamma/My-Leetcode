class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for frm,to,price in flights:
            graph[frm].append((to,price))

        heap = [(0,0,src)] #price,stops,city
        visited = {}

        while heap:
            price,stops,city = heapq.heappop(heap)

            if stops>k+1:
                continue
            
            if city==dst:
                return price

            if city in visited and visited[city]==stops:
                continue

            visited[city] = stops

            for nei,p in graph[city]:
                if nei not in visited or visited[nei]>stops:
                    heapq.heappush(heap,(price+p,stops+1,nei))

        return -1
        
