import math

def calc_area(a,b,c):
    s=(a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return area

def contr(area,total_area):
    return (area/total_area)*100

print("Enter the area for first triangle : ")
a1 = float(input("Enter side a : "))
b1 = float(input("Enter side b : "))
c1 = float(input("Enter side c : "))

print("Enter the area for second triangle : ")
a2 = float(input("Enter side a : "))
b2 = float(input("Enter side b : "))
c2 = float(input("Enter side c : "))

area1 = calc_area(a1,b1,c1)
area2 = calc_area(a2,b2,c2)

total_area = area1+area2

contri1 = contr(area1,total_area)
contri2 = contr(area2,total_area)

print(f"Area of first triangle : {area1:.2f}")
print(f"Area of second triangle : {area2:.2f}")
print(f"Total area : {total_area:.2f}")
print(f"Contribution of first triangle : {contri1:.2f}")
print(f"Contribution of second triangle : {contri2:.2f}")


#output
'''
Enter the area for first triangle : 
Enter side a : 3
Enter side b : 3
Enter side c : 3
Enter the area for second triangle :
Enter side a : 6
Enter side b : 6
Enter side c : 6
Area of first triangle : 3.90
Area of second triangle : 15.59
Total area : 19.49
Contribution of first triangle :  20.0
Contribution of second triangle :  80.0
'''