class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """ 

#Three points same line collinear
    #apply the  math formyla slope of AB = slope of BC
      
        p = points

        return (p[2][1]-p[1][1])*(p[1][0]-p[0][0]) != (p[2][0]-p[1][0])*(p[1][1]-p[0][1])



        
