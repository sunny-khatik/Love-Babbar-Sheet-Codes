# https://www.geeksforgeeks.org/function-to-find-number-of-customers-who-could-not-get-a-computer/
from collections import defaultdict
def runCustomerSimulation(n , s):
    d = defaultdict(lambda:-1)
    res = 0
    for i in s:
        if d[i] == -1 and n > 0:
            n-=1
            d[i]=1
        elif d[i] == 1:
            n+=1
            d[i] = -1
        elif d[i] == -1 and n == 0:
            res+=1
            d[i] = 0
    return res
            
print(runCustomerSimulation(5, "ABBAJJKZKZ"))
print(runCustomerSimulation(3, "GACCBDDBAGEE"))
print(runCustomerSimulation(3, "GACCBGDDBAEE"))
print(runCustomerSimulation(1, "ABCBCA"))
print(runCustomerSimulation(1, "ABCBCADEED"))
