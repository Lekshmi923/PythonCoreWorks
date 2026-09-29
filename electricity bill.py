#write a program to find the electricity bill based on the following criteria
#Units consumed

unit=int(input("Enter the units:"))
if unit<=100:
    print("Electricity bill is zero")
elif unit<=200:
    bill=(unit-100)*5
    print(bill)
elif unit<=300:
    bill=(100*5)+(unit-200)*10
    print(bill)
else:
    bill=(100*5)+(100*10)+((unit-300)*15)
    print(bill)