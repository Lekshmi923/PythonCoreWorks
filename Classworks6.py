# # # Q1.Define a function that takes 2 numbers and returns their product

def product(a,b):
    p=a*b
    return p
n1=int(input("Enter the number: "))
n2=int(input("Enter the number: "))
prod=product(n1,n2)
print(f"product is {prod}")

# # Q2.Define a function that takes a string and returns number of vowels

def vowel_count(s):
    vowel="aeiouAEIOU"
    count=0
    for i in s:
        if i in vowel:
            count=count+1
    return count

string=input("Enter the string: ")
c=vowel_count(string)
print(f"Number of vowel in {string} is {c}")

# # Q3.Define a function that takes length and breadth and returns area of
# #rectangle

def area(l,b):
    a=l*b
    return a

n1=int(input("Enter the length: "))
n2=int(input("Enter the breadth: "))
ar=area(n1,n2)
print(f"Area is {ar}")

# # Q4.Define a function that takes a list of numbers and creates a new list
# # with even numbers and returns the new list
# l=[45,78,90,12,35]

def newlist(l):
    new=[i for i in l if i%2==0]
    return new

list=[45,78,90,12,35]
nl=newlist(list)
print(nl)

# #Q5.Define a function that takes list of 3 digit numbers and returns a new list where
# # each value is the sum of digits of corresponding number in the original list.
# l = [123, 345, 111, 678, 134, 809]

def newlist(l):
    new=[]
    for i in l:
        sum = 0
        for j in str(i):
            sum=sum+int(j)
        new.append(sum)
    return new
list=[123, 345, 111, 678, 134, 809]
nl=newlist(list)
print(nl)

#Q6.Define a function that takes a list and returns a new list containing unique elemnets from the given
# list
# l=[12,34,78,12,67,34,90,23]

def newlist(l):
    new=[]
    for i in l:
        if i not in new:
            new.append(i)
    return new
lis=[12,34,78,12,67,34,90,23]
nl=newlist(lis)
print(nl)

#Q7.Define a function that takes 2 list as arguments and returns a new list containing common elements

list1=[12,34,56,78,90]
list2=[90,34,11,57,45]

def newlist(l1,l2):
    new=[i for i in l1 if i in l2]
    return new

list1=[12,34,56,78,90]
list2=[90,34,11,57,45]
nl=newlist(list1,list2)
print(nl)
