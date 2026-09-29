#sum of digits of a number

n=int(input("Enter the number: "))
num=n
s=0
while n>0:
    d=n%10
    s=s+d
    n=n//10
print(f"The sum of digits of {num} is {s}")