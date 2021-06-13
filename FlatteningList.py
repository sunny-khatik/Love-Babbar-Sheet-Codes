# https://practice.geeksforgeeks.org/problems/flattening-a-linked-list/1
def merge(a, b):
    result = None
    if a  == None:
        return b
    if b == None:
        return a
    if a.data < b.data:
        result = a
        result.bottom = merge(a.bottom,b)
    else:
        result = b
        result.bottom = merge(a, b.bottom)
    return result
    
def flatten(root):
        tmp=root
        res = tmp
        while tmp != None and tmp.next!= None:
            res = merge(res , tmp.next)
            tmp=tmp.next
        return res
