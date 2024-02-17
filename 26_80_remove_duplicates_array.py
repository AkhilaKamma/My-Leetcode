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
