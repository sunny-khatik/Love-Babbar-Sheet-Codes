# https://practice.geeksforgeeks.org/problems/zigzag-tree-traversal/1
# own solution easy see code only and problem in upeer link
def zigZagTraversal(root):
    # Your code here
    if root == None:
        return []
    ans= list()
    q = list()
    q.append(root)
    i = 0
    while len(q) > 0:
        n = len(q)
        l=list()
        for j in range(n):
            node = q.pop(0)
            l.append(node.data)
            if node.left != None:
                q.append(node.left)
            if node.right != None:
                q.append(node.right)
        # print(l)
        if i%2 != 0:
            l = l[::-1]
        ans+=l
        i+=1
    return ans
