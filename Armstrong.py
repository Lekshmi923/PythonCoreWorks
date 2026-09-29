#write a program to check whether a number is Armstrong number or not

n=int(input("Enter the number: "))
s=str(n)
sum=0
l=len(s)
for i in s:
    sum=sum+int(i)**l
if sum==n:
    print(f"{n} is an armstrong number")
else:
    print(f"{n} is not an armstrong number")