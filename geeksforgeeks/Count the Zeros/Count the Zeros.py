Given an array of size N consisting of only 0's and 1's. The array is sorted in such a manner that all the 1's are placed first and then they are followed by all the 0's. Find the count of all the 0's.

Example 1:

Input:
N = 12
Arr[] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0}
Output: 3
Explanation: There are 3 0's in the given array

#User function Template for python3

class Solution:
    def countZeroes(self, a, n):
        count=0
        for i in range(n):
          if a[i]==0:
            count+=1
        return count    
        # code here
if __name__ == '__main__':
  tc= int(input())
  while tc>0:
    n= int(input())
    arr=list(map(int, input().rstrip().split()))
    ob= Solution()
    ans=ob.countZeroes(arr,n)
    print(ans)
    tc-=1
