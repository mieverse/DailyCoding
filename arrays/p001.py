"""
p001 — Two Sum [Easy]
Aug 13, 2024 | Asked by Google | Topic: Arrays

Problem:
Given a list of numbers and a number k, return whether any two numbers
from the list add up to k.

Example:
    [10, 15, 3, 7], k=17 -> True (10 + 7)

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