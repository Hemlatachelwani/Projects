
Given an array A[] of size n. The task is to find the largest element in it.
 

Example 1:

Input:
n = 5
A[] = {1, 8, 7, 56, 90}
Output:
90
Explanation:
The largest element of given array is 90.
Solution:
max=0

Largest Element in Array Solution:

def largest( a, n):
  max=0    
  for i in range(0,n):
      if a[i]>max:
          max=a[i]
  return max
