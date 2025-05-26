## Problem 001
Aug 13, 2024
*This problem was recently asked by Google.*

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

## Solution (Python)

```python
def result(lis, k):
    n = len(lis)
    for i in range(n):
        for j in range(i + 1, n):
            if lis[i] + lis[j] == k:
                return True
    return False

a = [10, 15, 3, 7]
b = 17
print(result(a, b))  # Expected output: True
