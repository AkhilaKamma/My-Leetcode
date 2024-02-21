
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}

        for i,value in enumerate(nums):
            rem = target - value
            if rem in seen:
                return [i,seen[rem]]
            else:
                seen[value] = i


        
