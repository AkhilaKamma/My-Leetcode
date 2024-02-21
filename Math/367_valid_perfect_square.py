class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        #Time complexity- 0(n)
        
        x = num**0.5
        if(int(x) == x):
            return True
        return False

        #best approcah - O(logn)
        # binary search
        l, r = 1, num
        while l <= r:
            mid = (l + r) // 2
            if mid*mid == num:
                return True
            elif mid*mid < num:
                l = mid + 1
            else:
                r = mid - 1
        return False
        
