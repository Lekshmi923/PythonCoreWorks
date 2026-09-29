#write a program to check whether a number is positive or negative or zero

# n=int(input("Enter the number:"))
# if n>0:
#     print(f"{n} is positive")
# elif n<0:
#     print(f"{n} is negative")
# else:
#     print("Number is zero")

#write a program to find the greatest of three numbers

n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))
n3=int(input("Enter the third number:"))
if n1>n2 and n1>n3:
    print(f"{n1} is the greatest")
elif n2>n1 and n2>n3:
    print(f"{n2} is the greatest")
else:
    print(f"{n3} is the greatest")



