#sets are unordered, meaning the order of elements is not preserved
#sets do not allow duplicate elements
#sets are dynamic, meaning they can grow and shrink in size
#sets are represented by curly braces {}
#sets are mutable, meaning we can change their content

s = {'a','b','c' , 'b','d'} 
print(s) 

s = { True , False , 1 , 0}
print(s) # True and 1 are considered the duplicates , and False and 0 are considered the duplicates

s.add('e') # adding an element to the set
print(s)
s.remove(1) # removing an element from the set (This will raise error if the element is not found in the set)
print(s)
s.discard('c') # removing an element from the set without raising an error if the element is not found
print(s)

s.clear() # removing all elements from the set
print(s)


#Loops in sets
s = {'a','b','c','b','d'}
for i in s:
    print(i)

s = {'a','b','c','b','d',(1,2,3)}
for i in s:
    print(i)
s.clear()




# joining sets 
s1 = {'a','b','c'}
s2 = {'d','e','f'}
s1.update(s2) 
print(s1)
s1.clear()
s2.clear()
# OR
s1 = {'a','b','c'}
s2 = {'d','e','f'}
s3 = s1.union(s2)
print(s3)