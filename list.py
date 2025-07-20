ls = ['a','b','c'] # in list the negative indexing is like [-3,-2,-1]
x = 'Hello, World!'# in the string negative indexing is like  ......-3,-2-1,0=!
print(x[-5:-1])
print(ls[-1])
ls[2:3] = 'banana','hero'
print(ls)
ls[1] = ['banana' , 'hero']
print(ls)



ls1 = [1,2,3,4,5,6]
ls2 = ['a','s','d']
print(ls1+ls2)
print(ls1.extend(ls2))


ls3 = [14, 145, 34, 52, 4, 21, 4, 12, 4234, 1, 234]

ls3.reverse()
print("Reversed:", ls3)

ls3.sort()
print("Sorted ascending:", ls3)

ls3.sort(reverse=True)
print("Sorted descending:", ls3)
