#define a function that takes a number as an argument and return its square

# def square(num):
#     return num**2
# n=int(input("Enter the number:"))
# sq=square(n)
# print(sq)

# s=lambda n:n**2
# print(s(6))

# s=lambda n:n**3
# print(s(3))

# #sum of two numbers
# s=lambda a,b:a+b
# print(s(3,2))
#
# #product of three numbers
# s=lambda a,b,c:a*b*c
# print(s(3,2,5))
#
# #length of a string
# s=lambda string:len(string)
# print(s("good"))
#
# #square root of a number
# import math
# s=lambda n:math.sqrt(n)
# print(s(36))
#
# #first letter of a string
# s=lambda string:string[0]
# print(s("hello"))
#
# #last letter of a string
# s=lambda string:string[-1]
# print(s("hello"))
#
# #name value from dictionary
# d={"name":"anu","salary":100000,"age":27}
# s=lambda d,key:d[key]
# print(s(d,"name"))

# s=lambda a:a.get("name")
# d={"name":"anu","salary":100000,"age":27}
# print(s(d))
#
# #salary value from dictionary
# d={"name":"anu","salary":100000,"age":27}
# s=lambda d,key:d[key]
# print(s(d,"salary"))
#
# s=lambda a:a.get("salary")
# d={"name":"anu","salary":100000,"age":27}
# print(s(d))
#
# #add 10 to a number
# s=lambda n:n+10
# print(s(7))