# https://practice.geeksforgeeks.org/problems/roman-number-to-integer3201/1#

def romanToDecimal(s): #str in input
    # code here
    d = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" :50,
        "C": 100,
        "D" : 500,
        "M" : 1000
    }
    c=0
    n=len(s)
    prev = 0
    for i in range(n-1,-1,-1):
        if d[s[i]] >= prev:  # else we simply plus the values
            c+=d[s[i]]
        else: # if prev str charachter value is bigger then will  minus according to law
            c-=d[s[i]]
        prev = d[s[i]]
    return c
