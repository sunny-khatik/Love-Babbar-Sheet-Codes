d = { "a" : 3 , "c" : 1, "b":0 , "g" : -4}
d=sorted(d.items(),key=lambda x:x[0]) #sort the key of dictionary in ascending order
d=sorted(d.items(),key=lambda x:x[0] , reverse=True) #sort the key of dictionary in descending orde
# put x[1] it will sort the dictionary using alue accordingly.
d=sorted(d.items(),key=lambda x:x[1] , reverse=True) #sort dict by value in descending order
d=sorted(d.items(),key=lambda x:x[1]) #sort dict by value in ascending order.


#heap value dictionary
#this counter return the occurance of chrachter return this dictionary.
import collections
s = "abcdefghi"
cntr = collections.Counter(s)
for i in cntr:
    print(i, cntr[i])
    
    
    

