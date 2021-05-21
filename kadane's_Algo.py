#KADANES ALGO FOR MAXIMUM SUM SUBARRAY

# RETURN ONLY ANSWER
class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,a,size):
        ##Your code here
        max1 = a[0]
        sum = 0
        for i in range(size):
            sum+=a[i]
            max1 = max(max1 , sum)
            if sum < 0:
                sum = 0
        return max1
       



#FUNCTION RETRUN ANSWER AND ALSO PRINTS THE SUBARRAY.
class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,a,size):
        ##Your code here
        max1 = a[0]
        sum = 0
        flag = True
        start = 0
        for i in range(size):
            sum+=a[i]
            max1 = max(max1 , sum)
            if sum < 0:
                sum = 0
            else:
                if flag:
                    start = i
                    flag = False
        sum2=0
        k = start
        print(start)
        while True:
            if max1 == sum2:
                break
            sum2+=a[k]
            
            print(a[k],end=" ")
            k+=1
        print()
            
        return max1
