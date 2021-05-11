x , y= 10, 13 
print("First number {} is  and second number is {}".format(x, y))


del : del is used to delete a reference to an object. Any variable or list value can be deleted using del.

a = [1, 2, 3]
  
# printing list before deleting any value
print ("The list before deleting any value")
print (a)
  
# using del to delete 2nd element of list
del a[1]
  
# printing list after deleting 2nd element
print ("The list after deleting 2nd element")
print (a)




# one line else if statement
a = 10 if False else 0
print(a)


#round function
a = 10.5
b = -7.93
x = (round(a+b , 2))
print(x)
print(a+b)
