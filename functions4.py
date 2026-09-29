#create a new dictionary where keys are the elements in the dictionary and values are the count of elements

# l=[1,1,2,3,4,5,5,5,6,7]
# new={i:l.count(i) for i in l}
# print(new)

# l=[1,1,2,3,4,5,5,5,6,7]
# new={}
# for i in l:
#     new[i]=l.count(i)
# print(new)


#find the largest element
#find the second-largest element
#find the smallest element
#find the second-smallest element

# l=[34,12,56,89,90,11]
# print("Largest",max(l))
# print("Smallest",min(l))
# l.sort()
# print("Second Largest",l[-2])
# print("Second Smallest",l[1])

#create a new list of salary
#find the maximum salary
#create a new list of age
#find the minimum age

# l=[["arun",23,40000],["amal",24,50000],["anu",27,30000]]
# salary=[]
# for i in l:
#     salary.append(i[2])
# print(salary)
# print("Maximum salary is",max(salary))
#
# age=[]
# for i in l:
#     age.append(i[1])
# print(age)
# print("Minimum age is",min(age))

# l=[["arun",23,40000],["amal",24,50000],["anu",27,30000]]
# salary=[i[2] for i in l]
# print(salary)
# print("Maximum salary is",max(salary))
# age=[i[1] for i in l]
# print(age)
# print("Minimum age is",min(age))