# https://practice.geeksforgeeks.org/problems/first-non-repeating-character-in-a-stream1216/1
from collections import defaultdict
class Solution:
	def FirstNonRepeating(self, a):
	    d = defaultdict(lambda : 0)
	    ans = ""
	    mord = list()
	    for i in range(len(a)):
	        if d[a[i]] == 0:
	            mord.append(a[i])
	        d[a[i]]+=1
	        flag = 0
	        for j in range(len(mord)):
	            if d[mord[j]] == 1:
	                ans+=mord[j]
	                flag =1
	                break
	        if not flag:
	            ans+="#"
	    return ans
