#code library
# https://www.spoj.com/problems/ANARC05B/
if __name__ == "__main__":
    while True:
        l1 = list(map(int , input().split()))
        if l1[0] == 0:
            break
        l2 =  list(map(int , input().split()))
        s1 , s2 =0 ,0
        ans = 0
        i , j= 0  ,0
        while i < l1[0] and j < l2[0]:
            if l1[i+1] > l2[j+1]:
                s2+=l2[j+1]
                j+=1
            elif l1[i+1] < l2[j+1]:
                s1+=l1[i+1]
                i+=1
            else:
                ans= ans + max(s1 , s2) + l1[i+1]
                s1 ,s2=0,0
                i+=1
                j+=1
        while i < l1[0]:
            s1+=l1[i+1]
            i+=1
        while j < l2[0]:
            s2+=l2[j+1]
            j+=1
        ans+=max(s1,s2)
        print(ans)
                
