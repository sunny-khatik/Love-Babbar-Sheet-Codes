# https://www.geeksforgeeks.org/common-elements-in-all-rows-of-a-given-matrix/
def printCommonElements(mat):
    n = len(mat)
    m = len(mat[0])
    d = {}
    for i in mat[0]:
        d[i]=1
    for i in range(1,n):
        for j in range(m):
            if mat[i][j] in d and d[mat[i][j]] == i:
                d[mat[i][j]]+=1
    for i in d:
        if d[i] == n:
            print(i,end=" ")
    print()
                


mat = [[1, 2, 1, 4, 8],
       [3, 7, 8, 5, 1],
       [8, 7, 7, 3, 1],
       [8, 1, 2, 7, 9]]
 
printCommonElements(mat)
