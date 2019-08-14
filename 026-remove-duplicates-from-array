class Solution(Object):
  def removeDuplicates(self, A):
    if len(A) == 0: 
       return 0
       
    count = 0
    for i in range(len(A)):
      if A[count] != A[i]:
          count += 1
          A[count] = A[i]
   return count + 1
