# remove duplicates from list

# l=[1,1,1,2,3,3,4,5]
# print(list(set(l)))

#remove duplicates without set()

# l = [1,1,1, 2, 3, 3, 4, 5]
# new=[]
# for i in l:
#     if i not in new:
#         new.append(i)
# print(new)

# l = [1,1,1, 2, 3, 3, 4, 5]
# for i in l:
#     if l.count(i)>1:
#         l.remove(i)
# print(l)


# 3.Given two list
# print common elelments

# l1=[23,45,78,90,12,74]
# l2=[45,89,23,56,34]
# s1=set(l1)
# s2=set(l2)
# print(s1.intersection(s2))


#define a function that takes a list of numbers as arguments and print the count of even numbers,odd numbers and whose value is greater than 50
#l=[23,56,12,78,98,89,31,67]

# def count_num(l):
#     even=0
#     odd=0
#     greater=0
#     for i in l:
#         if i%2==0:
#             even=even+1
#             if i > 50:
#                 greater = greater + 1
#         else:
#             odd=odd+1
#             if i > 50:
#                 greater = greater + 1
#     print(f"Even numbers: {even}\nOdd numbers: {odd}\nNumbers greater than 50: {greater}")
# list=[23,56,12,78,98,89,31,67]
# count_num(list)


#define a function that takes a list of words as arguments and returns a new list of lengths
#l=["red","green","orange","yellow","blue"]

# def new_list(l):
#         new=[len(i) for i in l]
#         return new
#
# list=["red","green","orange","yellow","blue"]
# nl=new_list(list)
# print(nl)
