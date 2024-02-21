class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:


        #formula to remember for bitwise if x is a power of 2 then x&(x-1) = 0
        #for binary numbers  MSD = 1 if the number is a power of 2

        while right > left:
            right = right & (right-1)
        return right
