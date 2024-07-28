#1(a)
list = [56,98,78,65,25,45]
print("The numbers are : ")
for item in list:
    print(item)
sum=0
for item in list:
    sum=sum+item
print("Sum of the items in List is",sum)

print("\n\n")

#1(b)
list = [56,98,78,65,25,45]
print("The numbers are : ")
for item in list:
    print(item)
mul=1
for item in list:
    mul=mul*item
print("Product of the items in List is ",mul)

print("\n\n")

#1(c)
list = [56,98,78,65,25,45]
print("The numbers are : ")
for item in list:
    print(item)
largest=list[0]
for item in list:
    if(item>largest):
        largest=item
print("Largest of the items in List is ",largest)

print("\n\n")

#1(d)
list = [56,98,78,65,25,45]
print("The numbers are : ")
for item in list:
    print(item)
smallest=list[0]
for item in list:
    if(item<smallest):
        smallest=item
print("smallest of the items in List is ",smallest)

'''
The numbers are : 
56
98
78
65
25
45
Sum of the items in List is 367



The numbers are : 
56
98
78
65
25
45
Product of the items in List is  31302180000



The numbers are :
56
98
78
65
25
45
Largest of the items in List is  98



The numbers are :
56
98
78
65
25
45
smallest of the items in List is  25
'''