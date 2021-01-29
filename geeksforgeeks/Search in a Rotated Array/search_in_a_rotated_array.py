Given a sorted and rotated array A of N distinct elements which is rotated at some point, and given an element K. The task is to find the index of the given element K in the array A.

Input:
The first line of the input contains an integer T, denoting the total number of test cases. Then T test cases follow. Each test case consists of three lines. First line of each test case contains an integer N denoting the size of the given array. Second line of each test case contains N space separated integers denoting the elements of the array A. Third line of each test case contains an integer K denoting the element to be searched in the array.

Output:
Corresponding to each test case, output the index of the element found in the array.  If element is not present, then output -1.

#code
import os

def introTutorial(n,arr,ele):
    flag=0
    for i in range(len(arr)):
        if ele == arr[i]:
            print(i)
            flag=1
            
    if flag != 1:
      print("-1")

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n_t = int(input())
    for i in range(0,n_t):
       n = int(input())
       arr = list(map(int, input().rstrip().split()))
       ele = int(input())
       result = introTutorial(n,arr,ele)
    # print(str(result))
  
  
