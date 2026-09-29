# l=[10,20,30,40]
# for i in l:
#     for j in range(1,5):
#         print(i,end=" ")
#     print()

# 1 1 1
# 2 2 2
# 3 3 3

# for i in range(1,4):
#     for j in range(1,4):
#         print(i,end=" ")
#     print()

# 1 2 3
# 1 2 3
# 1 2 3

# for i in range(1,4):
#     for j in range(1,4):
#         print(j,end=" ")
#     print()

#nested sequence

# l=[["lion","tiger"],["cat","elephant"]]
# for i in l:
#     print(i)
#     for j in i:
#         print(j,end=" ")



# n=["kelly","alan","jenny"]
#
# #print the pattern
# # kelly kelly kelly
# # alan alan alan
# # jenny jenny jenny
#
# for i in n:
#     for j in range(1,4):
#         print(i,end=" ")
#     print()


# n=[1,2,3]
# qns=["what","when","why"]
#
# # print
# # 1
# # what when why
# # 2
# # what when why
# # 3
# # what when why
#
# for i in n:
#     print(i)
#     for j in qns:
#         print(j,end=" ")
#     print()



# d=[{'id':101,'name':'arun','age':25},
#    {'id':102,'name':'amal','age':23},
#    {'id':103,'name':'anu','age':24}]
#
# #print each student details
#
# for i in d:
#     print(i)
#     for j in i.values():
#         print(j,end=" ")
#     print()



# * * * *
# * * * *
# * * * *

# for i in range(1,4):
#     for j in range(1,5):
#         print("*",end=" ")
#     print()


# *
# * *
# * * *
# * * * *

# for i in range(1,5):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

# 2 2 2 2
# 4 4 4 4
# 6 6 6 6
# 8 8 8 8

# for i in range(2,9,2):
#     for j in range(1,5):
#         print(i,end=" ")
#     print()

# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1

# for i in range(5,0,-1):
#     for j in range(0,i):
#         print(i, end=" ")
#     print()

# * * * *
# * * *
# * *
# *

# for i in range(5,0,-1):
#     for j in range(1,i):
#         print("*", end=" ")
#     print()

# 1 1 1 1
# 2 2 2 2
# 3 3 3 3
# 4 4 4 4

# for i in range(1,5):
#     for j in range(1,5):
#         print(i,end=" ")
#     print()


# 1 0 0 0
# 0 2 0 0
# 0 0 3 0
# 0 0 0 4

# for i in range(1,5):
#     for j in range(1,5):
#         if(i==j):
#             print(i,end=" ")
#         else:
#             print(0,end=" ")
#     print()


# 1
# 1 0
# 1 0 1
# 1 0 1 0

# for i in range(1,5):
#     for j in range(1,i+1):
#         if(j%2!=0):
#             print("1",end=" ")
#         else:
#             print("0", end=" ")
#     print()


# 1
# 2 3
# 4 5 6
# 7 8 9 10

# num=1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(num,end=" ")
#         num=num+1
#     print()

# num=1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(num,end=" ")
#     num=num+1
#     print()



# *
# ***
# *****
# *******

# for i in range(1,8,2):
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()


# **
# ****
# ******
# ********

# for i in range(2,9,2):
#     for j in range(1,i+1):
#         print('*', end=" ")
#     print()


# 1
# 4 9
# 16 25 36
# 49 64 81 100

# k=1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(k**2,end=" ")
#         k=k+1
#     print()


# 1
# 3 5
# 7 9 11
# 13 15 17 19

# num=1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(num,end=" ")
#         num=num+2
#     print()

# A
# B C
# D E F
# G H I J

# k=ord('A') #65
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(chr(k),end=" ")
#         k=k+1
#     print()

# A
# B B
# C C C
# D D D D

# k=ord('A') #65
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(chr(k),end=" ")
#     k=k+1
#     print()

# A
# A B
# A B C
# A B C D

# for i in range(1,5):
#     k = ord('A')
#     for j in range(1,i+1):
#         print(chr(k),end=" ")
#         k=k+1
#     print()


#print all even numbers

# l=[23,65,42,80,56,41]
# for i in l:
#     if i%2==0:
#         print(i)

#print all prime numbers

# l=[23,65,42,80,56,41]
# for i in l:
#     for j in range(2,i):
#         if i%j==0:
#           break
#     else:
#         print(i)

#print all prime numbers in the range (1,100)

# for i in range(2,101):
#     for j in range(2,i):
#         if i%j==0:
#           break
#     else:
#         print(i)

#print all Armstrong numbers in the range(100,1001)

# for i in range(100,1001):
#     sum = 0
#     s=str(i)
#     l=len(s)
#     for j in s:
#         sum = sum + int(j) ** l
#     if sum == i:
#         print(i)


#    *
#   **
#  ***
# ****

# k=3*2
# for i in range(1,5):
#     for p in range(1,k+1): #extra loop for adding space
#         print(end=" ")
#     for j in range(1,i+1):  #loop for printing stars
#         print("*",end=" ")
#     k=k-2  #decrements space value
#     print()

#       *
#     *   *
#   *   *   *
# *   *   *   *

# k=3*2
# for i in range(1,5):
#     for p in range(1,k+1): #extra loop for adding space
#         print(end=" ")
#     for j in range(1,i+1):  #loop for printing stars
#         print("*",end="   ")
#     k=k-2  #decrements space value
#     print()



# *
# * *
# * * *
# * * * *
# * * *
# * *
# *


# for i in range(1,5):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
# for i in range(4,0,-1):
#     for j in range(1,i):
#         print("*", end=" ")
#     print()



#       *
#     * *
#   * * *
# * * * *
#   * * *
#     * *
#       *


# k=3*2
# for i in range(1,5):
#     for p in range(1,k+1): #extra loop for adding space
#         print(end=" ")
#     for j in range(1,i+1):  #loop for printing stars
#         print("*",end=" ")
#     k=k-2  #decrements space value
#     print()
# k=2
# for i in range(3,0,-1):
#     for p in range(1,k+1):
#         print(end=" ")
#     for j in range(1,i+1):
#         print("*",end=" ")
#     k=k+2
#     print()



#       *
#     *   *
#   *   *   *
# *   *   *   *
#   *   *   *
#     *   *
#       *


# k=3*2
# for i in range(1,5):
#     for p in range(1,k+1): #extra loop for adding space
#         print(end=" ")
#     for j in range(1,i+1):  #loop for printing stars
#         print("*",end="   ")
#     k=k-2  #decrements space value
#     print()
# k=2
# for i in range(3,0,-1):
#     for p in range(1,k+1): #extra loop for adding space
#         print(end=" ")
#     for j in range(1,i+1):  #loop for printing stars
#         print("*",end="   ")
#     k=k+2  #decrements space value
#     print()


# E
# D D
# C C C
# B B B B
# A A A A A

# k=ord('E') #65
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(chr(k),end=" ")
#     k=k-1
#     print()



# 1
# 2 1
# 3 2 1
# 4 3 2 1

# for i in range(1,5):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()


# 5
# 4 4
# 3 3 3
# 2 2 2 2
# 1 1 1 1 1

# for i in range(5,0,-1):
#     for j in range(6,i,-1):
#         print(i,end=" ")
#     print()

num=5
for i in range(1,6):
    for j in range(1,i+1):
        print(num,end=" ")
    num=num-1
    print()