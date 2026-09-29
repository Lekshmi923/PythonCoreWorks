#write a program to check whether the entered number is 2 digit 3 digit or 4 digit

n=int(input("Enter the number:"))
if n>=10 and n<=99:
    print(f"{n} is 2 digit number")
elif n>=100 and n<=999:
   print(f"{n} is a 3 digit number")
elif n>=1000 and n<=9999:
   print(f"{n} is a 4 digit number")
else:
    print(f"{n} is not a 3 digit or 2 digit number")
