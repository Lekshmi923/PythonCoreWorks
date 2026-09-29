#sum of two numbers

# def addition(n1,n2):
#     "Addition of two numbers"
#
#     s=n1+n2
#     print("sum",s)
#     return
# a=int(input("Enter a number: "))
# b=int(input("Enter a number: "))
# addition(a,b)

#Define a function that takes 3 arguments and find the simple interest.

# def SI(p,y,r):
#     si=(p*y*r)/100
#     print("Simple Interest",si)
#     return
# a=int(input("Enter the amount: "))
# b=int(input("Enter the number of years: "))
# c=int(input("Enter the rate: "))
# SI(a,b,c)

#Define a function that takes string and a character as arguments and print the count of the character

# def charcount(s,c):
#     count=0
#     for i in s:
#         if i==c:
#             count=count+1
#     print("count",count)
#     return
#
# string=input("Enter the string: ")
# ch=input("Enter the character: ")
# charcount(string,ch)


#sum of two numbers using return statement

# def addition(n1,n2):
#     "Addition of two numbers"
#     s=n1+n2
#     return s
#
# a=int(input("Enter a number: "))
# b=int(input("Enter a number: "))
# sum=addition(a,b)
# print(sum)

#define a function that takes 3 numbers and return the product as result call the function and print the result

def product(a,b,c):
    p=a*b*c
    return p
# n1=int(input("Enter the number: "))
# n2=int(input("Enter the number: "))
# n3=int(input("Enter the number: "))
# prod=product(n1,n2,n3)
# print(prod)

#define a function that takes string as argument and return a new dictionary where keys are words and valuses are length of each word.
#call the function and print the dictionary
#s="python coding is easy and fun"

# def dict(s):
#     new = {i: len(i) for i in s.split()}
#     return new
# string="python coding is easy and fun"
# nd=dict(string)
# print(nd)

def dict(s):
    new={}
    for i in s.split():
        new[i]=len(i)
    return new
string="python coding is easy and fun"
nd=dict(string)
print(nd)

