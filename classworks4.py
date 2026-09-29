#write a program to find BMI(Body Mass Index)
#
# BMI= weight in (kg)/ height**2 in (m)
#
#
# BMI	                 Status
# ≤ 18.4	             Underweight
# 18.5 - 24.9	         Normal
# 25.0 - 39.9	         Overweight
# ≥ 40.0	             Obese

w=float(input("Enter the weight in kg: "))
h=float(input("Enter the height in meter: "))
BMI=w/(h**2)
print(BMI)
if BMI<=18.4:
    print("Underweight")
elif BMI>18.4 and BMI<=24.9:
    print("Normal")
elif BMI>24.9 and BMI<=39.9:
    print("Overweight")
else:
    print("Obese")


#2.# A toy vendor supplies three types of toys:

# Battery Based Toys, Key-based Toys, and Electrical Charging Based Toys.

# The vendor gives a discount of 10% on orders for battery-based toys if the order is for more than Rs. 1000.

# On orders of more than Rs. 100 for key-based toys,a discount of 5% is given,

# and a discount of 10% is given on orders for electrical charging based toys of value more than Rs. 500.

# Assume that the numeric codes 1,2 and 3 are used for battery based toys, key-based toys, and electrical charging based toys respectively.

# Write a program that reads the product code and the order amount and prints out the net amount that the customer is required to pay after the discount.

pc=int(input("Enter the product code: "))
amt=int(input("Enter the order amount: "))
if pc==1:
    if amt>1000:
        net=amt-(amt*(10/100))
elif pc==2:
    if amt>100:
        net=amt-(amt*(5/100))
elif pc==3:
    if amt>500:
        net=amt-(amt*(10/100))
else:
    print(amt)
print(f"Net amount after discount is {net}")


#3 FIZZBUZZ problem

# if divisible by 3 only -print fizz
# if divisible by 5 only -print buzz
# if a number is divisible by 3 and 5
#     print fizzbuzz
#     otherwise -print the number

num=int(input("Enter the number: "))
if num%3==0 and num%5==0:
    print("fizzbuzz")
elif num%3==0:
    print("fizz")
elif num%5==0:
    print("buzz")
else:
    print(num)






