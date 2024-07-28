#3
for i in range(0,6):
    print(' '*(5-i),end='')
    for j in range (1,i+1):
        print(chr(64+j),end=' ')
    print()

'''    
    A 
   A B 
  A B C 
 A B C D 
A B C D E 
'''

for i in range(0,6):
    print(end='')
    for j in range (1,i+1):
        print("*",end='')
    print()

'''
*
**
***
****
*****
'''