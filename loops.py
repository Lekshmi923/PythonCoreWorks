#print all three digit numbers using while

# i=100
# while i<=999:
#     print(i)
#     i=i+1


# for i in range(100,999):
#     print(i)


colors=['red','green','blue','orange','yellow','black']

#print each color

# for i in colors:
#     print(i)

#colors contains letter b

# for i in colors:
#     if 'b' in i:
#         print(i)

#colors starting with letter g

# for i in colors:
#     if (i[0]=='g'):
#         print(i)

#colors ending with letter e

# for i in colors:
#     if (i[-1]=='e'):
#         print(i)

#first color starting with 'b'

# for i in colors:
#     if (i[0]=='b'):
#         print(i)
#         break




l=[23,45,12,78,90,51,75]

#print all numbers

# for i in l:
#     print(i)

#print all even numbers

# for i in l:
#     if i%2==0:
#         print(i)

#print those numbers that are divisible by 5

# for i in l:
#      if i%5==0:
#          print(i)

#stops the loop if i>50

# for i in l:
#     if i>50:
#         break
#     print(i)

#skips all even numbers

# for i in l:
#     if i%2==0:
#         continue
#     print(i)

#print the first even number whose value is greater than 50

# for i in l:
#     if i%2==0 and i>50:
#         print(i)
#         break

#count of all even numbers

# count=0
# for i in l:
#     if i%2==0:
#         count=count+1
# print(count)

#sum of list

# sum=0
# for i in l:
#     sum=sum+i
# print(sum)


#product of odd numbers

p=1
for i in l:
    if i%2!=0:
        p=p*i
print(p)

