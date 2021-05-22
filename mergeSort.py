class Solution:
    def _mergeSort(self,arr, temp_arr, left, right):
        if left < right:
            mid = (left + (right-1))//2 #right-1 for overflow
            self._mergeSort(arr, temp_arr,left, mid)
            self._mergeSort(arr, temp_arr,mid + 1, right)
            self.merge(arr, temp_arr, left, mid, right)

    def merge(self,arr, temp_arr, left, mid, right):
        i = left     # Starting index of left subarray
        j = mid + 1 # Starting index of right subarray
        k = left     # Starting index of to be sorted subarray
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp_arr[k] = arr[i]
                i += 1
            else:
                # Inversion will occur.
                temp_arr[k] = arr[j]
                j += 1
            k+=1
        while i <= mid:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        while j <= right:
            temp_arr[k] = arr[j]
            k += 1
            j += 1
        for loop_var in range(left, right + 1):
            arr[loop_var] = temp_arr[loop_var]


l=[-1,-6,4,3,7,1,3,2,-7]
o=Solution()
tmp=[0]*(len(l))
o._mergeSort(l,tmp,0,len(l)-1)
print(l)
