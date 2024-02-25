# This problem can be solved in both greedy and DP, but with greedy you can solve in a linear time O(n) for DP you need extra cache which is Memo
# memo[index] = True or False

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        goal = len(nums) - 1

        for i in range(len(nums)- 1,-1,-1):
            print(i)
            if i + nums[i] >= goal:
                goal = i
        return True if goal == 0 else False
