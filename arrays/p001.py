"""
p001 — Two Sum [Easy]
Asked by Google | Topic: Arrays

Problem:
Given a list of numbers and a number k, return whether any 
two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

What I Learned:
    -
"""

def twoSum(nums, k):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == k:
                return True
    return False


print(twoSum([10, 15, 3, 7], 17))