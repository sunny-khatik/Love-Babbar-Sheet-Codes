
def findMin(self, A):
  n = len(A)
  start , end = 0, len(A)-1
  minind = -1
  while start <= end:
      if A[start] <= A[end]:
          minind = start
          break
      mid = start + (end-start)//2
      prev = (mid-1+n)%n
      nextt = (mid+1)%n
      if A[mid] < A[prev] and A[mid] <= A[nextt]:
          minind = mid
          break
      elif A[start] <= A[mid]:
          start = mid+1
      elif A[mid] <= A[end]:
          end = mid-1
  return minind
