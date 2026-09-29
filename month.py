#write a program to print the number of days in a month

month=input("Enter the month:")
m1=['January','March','May','July','August','October','December']
m2=['April','June','September','November']
m3=['February']
if month in m1:
    print(f"{month} has 31 days")
elif month in m2:
    print(f"{month} has 30 days")
else:
    print(f"{month} has 28 or 29 days")