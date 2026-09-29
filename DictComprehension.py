#given a list
l=[1,2,3,4]
#create a dictionary where keys are numbers and values are squares of each number
new={i:i**2 for i in l}
print(new)

#create a dictionary where keys are numbers and values are cubes
new={i:i**3 for i in l}
print(new)

l=[10,20,30,40]
#create a dictionary where keys are index and values are each number itself
new={i:l[i] for i in range(0,len(l))}
print(new)

#given s string
s="python coding is easy and fun"
#create a dictionary where keys are words and values are length of each word
new={i:len(i) for i in s.split()}
print(new)