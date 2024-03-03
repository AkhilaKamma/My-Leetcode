class Solution:
    def jump(self, nums: List[int]) -> int:

        res = 0
        l = 0
        r = 0
       #Greedy approach
        while r < len(nums) - 1:
            fathest = 0
            for i in range(l, r + 1):
                fathest = max(fathest, i + nums[i])
            l = r + 1
            r = fathest
            res = res + 1
        return res
            
        
