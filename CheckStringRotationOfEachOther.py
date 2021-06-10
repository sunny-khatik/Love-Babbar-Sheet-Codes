# https://www.geeksforgeeks.org/a-program-to-check-if-strings-are-rotations-of-each-other/
def solve(s1, s2,n1, n2):
    if n1 != n2:
        return False
    tmp = s1+s1
    for i in range(len(tmp)-n1+1):
        if tmp[i:i+n1] == s2:
            return True
    return False
s1 =  "sunny"
s2 =    "unnsy"
print(solve(s1, s2,len(s1),len(s2)))
