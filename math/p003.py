"""
p202 — Integer Palindrome [Easy]
Asked by Palantir | Topic: Math

Problem:
Write a program that checks whether an integer is a palindrome. 
For example, 121 is a palindrome, as well as 888. 678 is not a palindrome. 
Do not convert the integer into a string.

What I Learned:
    - To reverse a number a mathematically
"""

def solution(n):
    if n < 0:
        return False

    original = n
    reversed = 0

    while n > 0:
        digit = n % 10
        reversed = reversed * 10 + digit
        n //= 10

    return original == reversed


print(solution(121))  
print(solution(888)) 
print(solution(678))