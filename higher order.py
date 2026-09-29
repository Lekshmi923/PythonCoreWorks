#Map

#create a new list of square

#map(function,sequence)
# l=[1,2,3,4,5]
# print(list(map(lambda x:x**2,l)))
# print(set(map(lambda x:x**2,l)))
# print(tuple(map(lambda x:x**2,l)))

# #Create a new list of cubes
# l=[1,2,3,4,5]
# print(list(map(lambda x:x**3,l)))
#
# #create a new list of cubes
# l=[1,2,3,4]
#
# #create a new list of square roots
#
# l=[25,36,81,100]
# print(list(map(lambda x:x**0.5,l)))
#
# #create a new list of lengths
# colors=['red','green','blue','yellow','black']
# print(list(map(lambda c:len(c),colors)))
#
# #create a new list of first characters
# print(list(map(lambda c:c[0],colors)))
#
# #create a new list of last characters
# print(list(map(lambda c:c[-1],colors)))
#
# #create a new list of reverse of each elemnt
# print(list(map(lambda c:c[::-1],colors)))
#
# #Given a list l=[23,78,12,56]
# #Add 10 to each element in the given sequence
# l=[23,78,12,56]
# print(list(map(lambda x:x+10,l)))
#
# ##given a list of dictionaries
# l=[{'empid':100,'name':'arun','salary':20000,'email':'arun@gmail.com'},
#    {'empid':101,'name':'amal','salary':25000,'email':'amal@gmail.com'},
#    {'empid':102,'name':'anu','salary':30000,'email':'anu@gmail.com'}]
#
# # # create a new list of emails
# print(list(map(lambda x:x["email"],l)))


#Filter

# l=[1,2,3,4,5,6,7,8,9,10]
# print(list(map(lambda x:x%2==0,l)))
# print(list(filter(lambda x:x%2==0,l)))
# print(list(filter(lambda x:x%5==0,l)))

# #given a list
# l=[23,65,89,12,20,33,85,40]
# #filter greater than 50
# print(list(filter(lambda x:x>50,l)))
# #filter even values less than 50
# print(list(filter(lambda x:x%2==0 and x<50,l)))
#
#
# #given a list
# fruits=["apple","orange","pineapple","grapes","avacado"]
# #filter elements whose length is greater than 5
# print(list(filter(lambda x:len(x)>5,fruits)))

#Reduce

import functools
l=[1,2,3,4,6,7]
print(functools.reduce(lambda a,b:a+b,l,0))
