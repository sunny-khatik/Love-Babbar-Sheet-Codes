
# https://leetcode.com/problems/merge-sorted-array/submissions/
class Solution:
    def findgap(self ,gap):
        if gap <= 1:
            return 0
        return (gap//2)+(gap%2)
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        gap = m+n
        gap= self.findgap(gap)
        while gap > 0:
            i = 0
            while gap+i < m:
                if nums1[i] > nums1[i+gap]:
                    nums1[i] , nums1[i+gap] = nums1[i+gap],nums1[i]
                i+=1
            j = gap-m if gap > m else 0
            while i < m and j <n:
                if nums1[i] > nums2[j]:
                    nums1[i], nums2[j] = nums2[j], nums1[i]
                i+=1
                j+=1
            if j < n:
                j = 0
                while j+gap < n:
                    if nums2[j] > nums2[j+gap]:
                        nums2[j] , nums2[j+gap] = nums2[j+gap], nums2[j]
                    j+=1
            gap=self.findgap(gap)
            
        for k in range(n):
            nums1[k+m] = nums2[k]
            
  
