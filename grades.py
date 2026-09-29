#write a program to print the grades in the following criteria

p=int(input("Enter the percentage:"))
if p>=91 and p<=100:
    print('The grade is A')
elif p>=81 and p<=90:
    print('The grade is B')
elif p>=71 and p<=80:
    print('The grade is C')
elif p>=61 and p<=70:
    print('The grade is D')
else:
    print("The grade is E")