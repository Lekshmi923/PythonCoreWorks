#Positional Arguments

# def fun(n,a):
#     print("Name",n)
#     print("Age",a)
# fun("Arun",23)
# fun("Arun")          #error
# fun(23,"Arun") #positional change

#Keyword Arguments

# def fun(n,a):
#     print("Name",n)
#     print("Age",a)
# fun(n="Arun",a=23)
# fun(a=23,n="Arun")

#Default Arguments

# def fun(n,a=22):
#     print("Name",n)
#     print("Age",a)
# fun(n="Arun",a=26)
# fun(n="Anusree")

#Variable length\Arbitary Arguments

#Variable length\Arbitary Positional Arguments(*args)

# def fun(*args):
#     print(args)
# fun(10,20)
# fun(1,2,3,4,5)

#Variable length\Arbitary Keyword Arguments(*kwargs)

# def fun(**kwargs):
#     print(kwargs)
# fun(a=10,b=20)
# fun(a=2,b=4,c=6,d=8)


#Define a function to find the the sum of numbers using arbitary positional arguments

def add(*args):
    sum=0
    for i in args:
        sum=sum+i
    print(sum)
add(2,3)
add(2,3,4)
add(10,20,30,40,50)