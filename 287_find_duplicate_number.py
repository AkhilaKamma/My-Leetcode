class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort() # Time: O(nlogn)
        
        length = len(nums)

        for i in range(1, length):
            if nums[i] == nums[i - 1]:
                return nums[i]

        return length


# For Linear - Time Complexity
