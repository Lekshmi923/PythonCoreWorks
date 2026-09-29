#write a program to find the position of a specific character in a string

# s=input("Enter the string:")
# ch=input("Enter the character:")
# if ch in s:
#     p=s.index(ch)
# print(f"Position of {ch} is {p}")

#write a program to find the count of a specific character in a string
# s=input("Enter the string:")
# ch=input("Enter the character:")
# if ch in s:
#     c=s.count(ch)
# print(f"Count of {ch} is {c}")

#write a program to create a new dictionary where keys are letters and values are the count of each letter

# s=input("Enter the string:")
# new={i:s.count(i) for i in s if i.isalpha()}
# print(new)

#Write a program to create a new list with 5 random 3-digit numbers

# new=[]
# import random
# for i in range(1,6):
#     a=random.randint(100,1000)
#     new.append(a)
# print(new)

#write a program to create a 5 digit otp number

# import random
# otp=random.randint(10000,100000)
# print(f"OTP number is {otp}")


#write a program to find the count of letters,spaces and digits in a string
# s=input("Enter the string:")
# cl=0
# cs=0
# cd=0
# for i in s:
#     if i.isalpha():
#         cl=cl+1
#     elif i.isdigit():
#         cd=cd+1
#     elif i.isspace():
#         cs=cs+1
#     else:
#         print("None")
# print(f"letters:{cl}\n digit:{cd}\n space:{cs}")


#write a program to create a new dictionary where keys are words and values are length of each word

s=input("Enter the string:")
new={i:len(i) for i in s.split()}
print(new)