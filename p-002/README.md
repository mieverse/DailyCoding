## Problem 002 [Hard]
Aug 14, 2024 | *This problem was asked by Uber.*

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?

## Solution (Python)

```python
def product(arr):
  new = []
  for i in range(0, len(arr)): # to iterate the array
    curr = i
    sum = 1
    for j in range(0, len(arr)): # to find the product
      if j != curr:
        sum = sum*arr[j]
    new += [sum]
  return new

a = [1, 2, 3, 4, 5]
print(product(a)) # Expected output: [120, 60, 40, 30, 24]
b= [3, 2, 1] 
print(product(b))  # Expected output: [2, 3, 6]
	
	

