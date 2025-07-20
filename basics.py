# print("hello")

# # if else
# age = 18
# if(age>=18):
#     print("Adult")
# else:
#     print("Minor")

# #Assigning multi valaues to multi variables 
# name,sex,country  = "Dhruv","Male","India"
# print(name)
# print(sex)
# print(country)

# #Assigning single values to multi variables 
# x = y = z = "hello"
# print(x+y+z)

# #List
# fruits = ["apple" , "banana" , "orange"]
# print(fruits)
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])


# #Unpack List and assign to variables 
# # x , y = fruits      ERROR : too many values to unpack
# # print(x+" "+y)

# #correct unpacking
# x , y , z = fruits
# print(x+" "+y+" "+z)


# #Casting in pyhton 
# x = int(1) #1
# y = str(fruits[1]) # banana
# z = bool(fruits[2]) # true
# print(x)
# print(y)
# print(z) # true because the value of the fruits[2] is not null
# print(x,y,z) #1 banana True


# x = 1
# y = 5 
# print(x+y)



# x = input("Enter your name : ")
# def func(x):
#     print("hello "+x)
#     for i in range(len(x)):
#         if x[i] == "D":
#             continue
#         print(x[i])
# func(x)






x  = int(input("Enter a number: "))
def fact(x):
    print(x)
    if x<=1:
        return 1
    else :
        return x*fact(x-1)
    print(x)

print(fact(x))