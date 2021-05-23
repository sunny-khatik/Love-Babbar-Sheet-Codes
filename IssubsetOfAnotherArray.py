# https://www.geeksforgeeks.org/find-whether-an-array-is-subset-of-another-array-set-1/
# see all another approches.
def isSubset( a1, a2, n, m):
    s= set()
    for i in a1:
        s.add(i)
    bool = "Yes"
    for i in a2:
        if i not in s:
            bool = "No"
            break
    return bool
