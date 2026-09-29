
# def addition():
#     "Addition of two numbers"
#
#     n1=int(input("Enter a number: "))
#     n2=int(input("Enter a number: "))
#     s=n1+n2
#     print("sum",s)
#     return
# addition()

#Define a function to display "hello your name"

# def display():
#     name=input("Enter your name: ")
#     print("hello",name)
#     return
# display()

#Define a function to find the count of a specific character in a string

# def charcount():
#     count=0
#     string=input("Enter the string :")
#     c=input("Enter the character:")
#     for i in string:
#         if i==c:
#             count=count+1
#     print("count",count)
#     return
# charcount()

#Define a function to find the factorial of a number

# def factorial():
#     fact=1
#     num=int(input("Enter the number: "))
#     for i in range(1,num+1):
#         fact=fact*i
#     print("Factorial :",fact)
#     return
# factorial()

#Define a function to check whether a number is Armstrong or not

# def armstrong():
#     num=int(input("Enter the number: "))
#     s=str(num)
#     sum = 0
#     l = len(s)
#     for i in s:
#         sum = sum + int(i) ** l
#     if sum == num:
#         print(f"{num} is an armstrong number")
#     else:
#         print(f"{num} is not an armstrong number")
#     return
# armstrong()

#Define a function to  check whether a number is prime or not

# def prime():
#     num=int(input("Enter the number: "))
#     for i in range(2,num):
#         if num%i==0:
#             print(f"{num} is not prime number")
#             break
#     else:
#         print(f"{num} is a prime number")
#     return
# prime()

#Define a function to find the factors of a number

def factor():
    num=int(input("Enter the number: "))
    for i in range(1,num+1):
        if num%i==0:
            print(i)
    return
factor()

