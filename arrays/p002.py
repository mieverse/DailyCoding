"""
p002 — Product Except Self [Hard]
Aug 14, 2024 | Asked by Uber | Topic: Arrays

Problem:

Given an array of integers, return a new array such that each element
at index i is the product of all the numbers in the original array
except the one at i.

Example:
    [1, 2, 3, 4, 5] -> [120, 60, 40, 30, 24]
    [3, 2, 1]       -> [2, 3, 6]

Follow-up: what if you can't use division?

What I Learned:
    -
"""

def product(arr):
    result = []
    for i in range(len(arr)):
        prod = 1
        for j in range(len(arr)):
            if j != i:
                prod *= arr[j]
        result.append(prod)
    return result


print(product([1, 2, 3, 4, 5]))  # Expected: [120, 60, 40, 30, 24]
print(product([3, 2, 1]))        # Expected: [2, 3, 6]