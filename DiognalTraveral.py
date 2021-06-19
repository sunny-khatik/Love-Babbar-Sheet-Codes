# https://practice.geeksforgeeks.org/problems/diagonal-traversal-of-binary-tree/1
# code library
def diagonal(root):
    ans = list()
    q = list()
    q.append(root)
    while len(q) > 0:
        root = q.pop(0)
        while root != None:
            if root.left != None:
                q.append(root.left)
            ans.append(root.data)
            root=root.right
    return ans
