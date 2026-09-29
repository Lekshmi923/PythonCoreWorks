#write a basic calculator program to perform arithmetic operations


n1=int(input("Enter the first number:"))
n2=int(input("Enter the first number:"))
op=input("Enter the operation:")
if op=="+":
    n3=n1+n2
    print(f"sum is {n3}")
elif op=="-":
    n3=n1-n2
    print(f"difference is {n3}")
elif op=="*":
    n3=n1*n2
    print(f"product is {n3}")
elif op=="/":
    n3=n1/n2
    print(f"quotient is {n3}")
elif op=="%":
    n3=n1%n2
    print(f"remainder is {n3}")
elif op=="//":
    n3=n1//n2
    print(n3)