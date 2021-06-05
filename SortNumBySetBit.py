# https://practice.geeksforgeeks.org/problems/sort-by-set-bit-count1153/1
# count sort based solution

class Solution:
    def sortBySetBitCount(self, arr, n):
        # Your code goes here
        arr_32 = [[] for i in range(32)]
        for i in range(n):
            arr_32[bin(arr[i]).count("1")].append(arr[i])  #append according to number of 1 in eleemnt
        j=0
        for i in range(31,-1,-1):  #trverse from left to right and add in an array
            num_store = arr_32[i]
            for k in range(len(num_store)):
                arr[j]=num_store[k]
                j+=1
        return arr
