# My-Leetcode
**Recersive approach to generate all combinations to get the target number**

def combination_sum_helper(nums, target, index, path, result):
    if target == 0:
        result.append(path)
        return
    if target < 0:
        return
    for i in range(index, len(nums)):
        combination_sum_helper(nums, target - nums[i], i + 1, path + [nums[i]], result)
      
**Recersive approach to generate all combinations to get the target number by repeating the given number any number of times**
def combination_sum_helper(nums, target, index, path, result):
    if target == 0:
        result.append(path)
        return
    if target < 0:
        return
    for i in range(index, len(nums)):
        combination_sum_helper(nums, target - nums[i], i, path + [nums[i]], result)

        
def combination_sum(nums, target):
    result = []
    nums.sort()
    combination_sum_helper(nums, target, 0, [], result)
    return result
    
result = combination_sum(per_list, n)

**Binary search algorithm to find Perfect squares or square root of a number - O(logn)**
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
        for i in range(1,n+1):
            if isPerfectSquare(i):
                per_list.append(i)
        print(per_list)




