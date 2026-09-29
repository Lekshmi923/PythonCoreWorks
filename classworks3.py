#write a program to check whether two  entered numbers are equal or not

# n1=int(input("Enter the first number:"))
# n2=int(input("Enter the second number:"))
# if n1==n2:
#     print(f"{n1} and {n2} are equal")
# else:
#     print(f"{n1} and {n2} are not equal")

#write a program to check whether two  entered words are equal or not

# w1=input("Enter the first word:")
# w2=input("Enter the second word:")
# if w1==w2:
#     print(f"{w1} and {w2} are equal")
# else:
#     print(f"{w1} and {w2} are not equal")

#write a program to find the maximum of two numbers

# n1=int(input("Enter the first number:"))
# n2=int(input("Enter the second number:"))
# if n1>n2:
#     print(f"{n1} is greater")
# else:
#     print(f"{n2} is greater")


#write a program to whether the entered character is vowel or not

# char=input("Enter the character:")
# vowel="aeiouAEIOU"
# if char in vowel:
#     print(f"{char} is a vowel")
# else:
#     print(f"{char} is not a vowel")

#write a program to check whether the entered country name contains "land"

# country=input("Enter the country name:")
# if "land" in country:
#     print(f"{country} contains land")
# else:
#      print(f"{country} does not contain land")

#write a program to check  whether the entered number is 3 digit or not

# n=int(input("Enter the number:"))
# if n>=100 and n<=999:
#     print(f"{n} is a 3 digit number")
# else:
#     print(f"{n} is not a 3 digit number")

#write a program to check whether the entered string is palindrome or not

# string=input("Enter the string:")
# rev=string[::-1]
# if string==rev:
#     print(f"{string} is a palindrome")
# else:
#     print(f"{string} is not a palindrome")

#write a program to check whether the number is present in the given list

# l=[2,5,6,7,9]
# print(l)
# n=int(input("Enter the value:"))
# if n in l:
#     print(f"{n} is present")
# else:
#     print(f"{n} is not present")

#write a program to check whether a key is present in the dictionary

# d={101:'Arun',102:'Amal',103:'Anu'}
# print(d)
# key=int(input("Enter the key:"))
# if key in d:
#     print(f"{key} is in the dictionary")
# else:
#     print(f"{key} is not in the dictionary")

#write a program to check if the given password is strong/weak(if the length is less than 8 then the password is weak

p=input("Enter the password:")
if len(p)>8:
    print("password is strong")
else:
    print("password is not strong")