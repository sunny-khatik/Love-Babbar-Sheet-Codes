# See binary beats video for Solution
# https://practice.geeksforgeeks.org/problems/factorials-of-large-numbers2508/1
class Solution:
    def factorial(self, N):
        q = 2
        l = [0]*(10000)
        length = 1
        l[0]=1
        x = 0
        num = 0
        while q <= N:
            x=0
            while x < length:
                l[x] = l[x]*q + num
                num = l[x]//10
                l[x]=l[x]%10
                x+=1
            while num != 0:
                l[length]=num%10
                num = num//10
                length+=1
            q+=1
        return l[length-1::-1]
