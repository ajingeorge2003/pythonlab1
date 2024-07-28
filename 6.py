num=int(input("Enter a 4 digit number : "))
rev=num
if len(str(num))==4:
    print("Sum of the digits : ")
    sum=0
    for i in range(0,4):
        rem=num%10
        sum=sum+rem
        num=int(num/10)
    print(sum)

    print("Reverse of the String : ")
    print(int(str(rev)[::-1]))

else:
    print("Enter 4 digit number")



#output
'''
Enter a 4 digit number : 2347
Sum of the digits :
16
Reverse of the String :
7432
'''