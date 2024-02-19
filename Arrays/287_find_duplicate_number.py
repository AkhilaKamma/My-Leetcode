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
class Solution(object):
    def findDuplicate(self, nums):
        seen = set()
        for element in nums:
            if element in seen:
                return element
            seen.add(element)
        return False


##Next method using HashMap (best Runtime)
#HashMap provide fast insertion deletion and Look up times
class Solution(object):
    def findDuplicate(self, nums):
        hashMap = {}
        for ele in nums:
            if ele in hashMap:
                return ele
            hashMap[ele] = 1
        
        
