class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        for i in nums:
            if i not in seen:
                seen.add(i)
        
        test = list(seen)
        test.sort()
        print(test)
        
        j = 0
        for i in test:
            nums[j]  = i
            j = j + 1
        return j


# In place modification of array , try to use Left and right pointers
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        for right in range(len(nums)):
            if nums[left]!=nums[right]:
                left+=1
                nums[left], nums[right] = nums[right], nums[left]

        return left+1


#80... similar style

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        left = right = 0

        while right < len(nums):
            count = 1
            while right + 1 < len(nums) and nums[right] == nums[right + 1]:
                right = right + 1
                count = count + 1

            for i in range(min(2,count)):
                nums[left] = nums[right]
                left = left + 1 

            right = right + 1          
        return left


