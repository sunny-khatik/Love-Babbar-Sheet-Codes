# Code library
# https://www.geeksforgeeks.org/print-left-view-binary-tree/
def LeftView(root):
    if root == None:
        return []
    l = list()
    q = list()
    q.append(root)
    while len(q) > 0:
        n = len(q)
        for i in range(n):
            tmp = q.pop(0)
            if i == 0:
                l.append(tmp.data)
            if tmp.left != None:
                q.append(tmp.left)
            if tmp.right != None:
                q.append(tmp.right)
    return l
