#List comprehension

# l=[1,2,3,4,5]
# #create a new list with squares of each element
#
# new=[i**2 for i in l]
# print(new)
#
# #create a new list with cubes of each element
#
# new=[i**3 for i in l]
# print(new)
#
# new=[5 for i in l]
# print(new)
#
# new=[i+1 for i in l]
# print(new)


# l=[23,46,55,11,78,90,24]
# #create a new list with even values
#
# new=[i for i in l if i%2==0]
# print(new)
#
# #create a new list with numbers whose value is greater than 50
#
# new=[i for i in l if i>50]
# print(new)


# l=[12,45,34,67,90]
# # create a new list with even values
# new=[i for i in l if i%2==0]
# print(new)
#
# #create a new list with values greater than 50
# new=[i for i in l if i>50]
# print(new)

#Given  a list
# colors=['red','green','blue','orange']
# # create a new list with first letter of each color

# new=[i[0] for i in colors]
# print(new)

# # create a new list with length of each color

# new=[len(i) for i in colors]
# print(new)
#
# #create a new list of square roots
# l=[25,36,81,100]
# new=[i**(0.5) for i in l]
# print(new)



# colors=['red','green','blue','yellow','black']
# #create a new list of lengths
# new=[len(i) for i in colors]
# print(new)
# #create a new list of first characters
# new=[i[0] for i in colors]
# print(new)
# #create a new list of last characters
# new=[i[-1] for i in colors]
# print(new)
# #create a new list of reverse of each element
# new=[i[::-1] for i in colors]
# print(new)


# #Given a list
# l=[23,78,12,56]
# #Add 10 to each element in the given sequence
# new=[i+10 for i in l]
# print(new)


##given a list of dictionaries
l=[{'empid':100,'name':'arun','salary':20000,'email':'arun@gmail.com'},
    {'empid':101,'name':'amal','salary':25000,'email':'amal@gmail.com'},
    {'empid':102,'name':'anu','salary':30000,'email':'anu@gmail.com'}]
#
# # create a new list of emails
new=[i['email'] for i in l]
print(new)

# # #create a new list with square root of each element
l=[25,16,9,36]
new=[int(i**(0.5)) for i in l]
print(new)

# #Given a dictionary
d={'arun':25,'amal':34,'akhil':26,'anu':21}
# # create a list of names
new=[i for i in d]
print(new)

# # create a list of marks
new=[i for i in d.values()]
print(new)
#
# #Given a list
l=[23,56,12,89,-34,-23,-67,-43,9.7,4.5,'hello','world']

# #create a list of string values
new=[i for i in l if type(i)==str]
print(new)
# #create a list of floats
new=[i for i in l if type(i)==float]
print(new)
# #create a list of positive numbers
new=[i for i in l if type(i)!=str and i>0]
print(new)
#
#
# #Given a list
fruits=['apple','orange','pineapple','avocado','grapes']
# #create a new list with elements whose length is greater than 6
new=[i for i in fruits if len(i)>6]
print(new)

# #create a new list with elements whose value is divisible by 3 in range(1,101)
new=[i for i in range(1,101) if i%3==0]
print(new)

# Given
s="python coding  is easy and fun"
# # create a new list with only vowels
vowels="aeiouAEIOU"
new=[i for i in s if i in vowels]
print(new)