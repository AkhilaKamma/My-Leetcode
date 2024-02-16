class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        a = Counter(arr) # Time: O(n), Space: O(n)

        sorted_list = sorted(arr, key=lambda x:(a[x],x)) # Time: O(n log n)

        print(sorted_list)

        sorted_list = sorted_list[k:] # Time: O(n)

        return len(set(sorted_list)) # Time: O(n), Space: O(n)


#Time complexity: O(n logn)

#Space Complexity: O(n)
        
