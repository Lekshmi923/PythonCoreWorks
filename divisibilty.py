#check whether a number is divisible by 2 and 3/divisible 2 and not by 3/divisible by 3 and not by 2/not divisible by 2 and 3

n=int(input("Enter the number:"))
if n%2==0:
    if n%3==0:
        print(f"{n} is divisible by 2 and 3")
    else:
        print(f"{n} is divisible by 2 and not by 3")
elif n%3==0:
    if n%2==0:
        print(f"{n} is divisible by 3 and 2")
    else:
        print(f"{n} is divisible by 3 and not by 2")
else:
    print(f"{n} is not divisible by 3 and 2")