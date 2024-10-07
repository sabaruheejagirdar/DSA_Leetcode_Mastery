""" 
LEETCODE: 31- Next Permutation
For example, for arr = [1,2,3], the following are all the permutations of arr: 
[1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].

Example1
Input: nums = [1,2,3]
Output: [1,3,2]

Example2
Input: nums = [2,1,5,4,3,0,0]
Output: [2,3,0,0,1,4,5]
"""
"""
APPROACH:
1. Find break point from the end of array such that current number lesser tha next
   A[i] < A[i+1] 
   Ex2: [..1,5,...]
2. Find the next greater element to index and swap it. 
   Ex2: Next greater than 1 i.e. 3 and swap => [2,3,....,1,..]
3. Sort or reverse the right half.
   Ex2: [2,3,0,0,1,4,5]
"""

def nextPermutation(nums): 
    n = len(nums)

    #Step1: Find the break point:
    index = -1
    for i in range(n-2,-1,-1):
        if nums[i] < nums[i+1]:
            index = i
            break
    ## If break doesn't exists
    if index == -1:
        nums.reverse()
        return nums
    
    #Step2: Find the next greater element abd swap it with num[index]
    for i in range(n-1, index,-1):
        if nums[i] > nums[index]:
            nums[i], nums[index] = nums[index], nums[i]
            break

    #Step3: Reverse the right half
    nums[index+1:] = reversed(nums[index+1:])
    
    return nums

nums = [2,1,5,4,3,0,0]
# nums = [5,4,3,2,1]
result = nextPermutation(nums)
print(result)