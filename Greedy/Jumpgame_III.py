#DFS stack, BFS - Queue, Memo = {}

#here using DFS

class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        visited, stack, n = set(), [], len(arr)

        stack.append(start)
        
        while stack:
            idx = stack.pop()

            if idx in visited:
                continue
            
            curr = arr[idx]
            if curr == 0:
                return True

            visited.add(idx)
            
            if idx + curr < n:
                stack.append(idx + curr)
            if idx - curr >= 0:
                stack.append(idx - curr)
        return False
        
