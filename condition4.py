#write a program to check whether the user entered number is positive even or odd/negative even or odd

n=int(input("Enter the number:"))
if n>0:
    print("Positive number")
    if n%2==0:
        print("Even number")
    else:
        print("Odd number")
else:
    print("Negative number")
    if n%2==0:
        print("Even number")
    else:
        print("Odd number")