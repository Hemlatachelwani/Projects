Given a matrix of size n x m, where every row and column is sorted in increasing order, and a number x. Find whether element x is present in the matrix or not.

Example 1:

Input:
n = 3, m = 3, x = 62
matrix[][] = {{ 3, 30, 38},
              {36, 43, 60},
              {40, 51, 69}}
Output: 0
Explanation:
62 is not present in the matrix, 
so output is 0.

Solution:
#User function Template for python3

def search(matrix, n, m, x): 
	# code here 
	flag=0
	for i in range(0,n):
	    for j in range(0,m):
	        if matrix[i][j]==x:
	            flag=1
	        else:
	            pass
	if flag==1:
	  return(True)
	else:
	  return(False)
	
