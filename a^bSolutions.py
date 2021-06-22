# log(n) time complexity b negative as well as positive but note important thing here.
def solve(a,b):
    if (b) == 0:
        return 1
    tmp = solve(a,int(b/2))  #very important if -1//2 = -0.5 round it ti -1 again and again so it will go in loop
    if b%2 == 0:
        return tmp*tmp
    else:
        if b > 0:
            return a*tmp*tmp
        else:
            return (tmp*tmp)/a 

x, y = 8, -1  #works for both the cases.
print((solve(x, y)))
