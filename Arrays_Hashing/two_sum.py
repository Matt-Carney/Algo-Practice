# https://leetcode.com/problems/two-sum/
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""

# Test Case
nums = [2,7,11,15]
nums2 = [2,11,15,7]
target = 9
output = [0,1]


### Brute Force
def twosum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return i, j

twosum(nums, target)
# Time complexity: O(N^2)
# Space complexity: O(1)


# Optimized for time
def optimal_twosum(nums: list[int], target: int) -> list[int]:
    d = {} #diff val : index
    for i, value in enumerate(nums):
        print(d)
        diff = target - value
        if diff in d:
            return [d[diff], i]
        d[value] = i

optimal_twosum(nums2, target)
# Time complexity: O(N) (inserting to hasmap is O(1) * N times)
# Space complexity: O(1)






