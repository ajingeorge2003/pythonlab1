#2
A = ['abc','xyz','aba','1221']
print("The items are : ")
for item in A:
    print(item)
smallest=list[0]
for index, string in enumerate(A):
    if string[0]==string[-1]:
        print("Index : ",index," Item : ",string)


'''
The items are : 
abc
xyz
aba
1221
Index :  2  Item :  aba
Index :  3  Item :  1221
'''