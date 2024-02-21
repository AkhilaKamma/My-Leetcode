class Solution(object):

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        def isPerfectSquare(num):
            l = 0
            r = num
            while l <= r:
                mid = (l+r) // 2
                if mid * mid == num:
                    return True
                elif mid * mid > num:
                    r = mid - 1
                else:
                    l = mid + 1
            return False

        per_list = []
        for i in range(1,n):
            if isPerfectSquare(i):
                per_list.append(i)
        print(per_list)

        minCount = 10**4
        target = n
        for i in per_list:
            if i % n == 0:
                return min(minCount, int(i/n))
            else:
                target = target - i
                count = count + 1
                if target == 0:
                    return min(minCount,count)
        return False



        
