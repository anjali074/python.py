#Q-1-cDemonstart the working of the following functions in python?
#id() function
a = 5
b = 7
c = a
print("Id of a", id(a))    
print("Id of b", id(b))    
print("Id of c", id(c))    
print("a and c have the same Id", id(a) == id(c))   

 #type() function
x = 20
y = "Anjali"
z = [1, 2, 4]

print("type of x", type(x))    
print("type of y", type(y))    

# range() function
print("range with one argument (5)")
for i in range(5):  
    print(i)
print("range with two arguments (2, 7)")
for i in range(2, 5):  
    print(i)
print("range with three arguments (1, 10, 2)")
for i in range(1, 20, 2):   
    print(i)
