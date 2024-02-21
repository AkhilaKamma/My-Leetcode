class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        if n == 1:
            return True
        # Trying to solve in a binary way , every power of 2 has only one digit in its binary space
        bool_val = False
        for i in range(31):
            if n & 1 == 1:
                if bool_val == True:
                    return False
                bool_val = True
            n = n >> 1
        return True
        
