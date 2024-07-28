months = [
    ("January", 31),
    ("February", 28),
    ("March", 31),
    ("April", 30),
    ("May", 31),
    ("June", 30),
    ("July", 31),
    ("August", 31),
    ("September", 30),
    ("October", 31),
    ("November", 30),
    ("December", 31)
]

def is_leapyear(year):
    if year%4==0 and year%100!=0 : 
        return True
    return False

month_name = input("Enter the Month name : ").strip()

days=0
for month,days_in_month in months:
    if month.lower() == month_name.lower():
        days = days_in_month
        if month.lower() == "february":
            year=int(input("Enter the year : "))
            if is_leapyear(year):
                days = 29
        break

if days>0:
    print("The number of days in",month_name,"is",days)
else:
    print("Invalid month : ",month_name)

'''
Enter the Month name : January
The number of days in February is 29

Enter the Month name : February
Enter the year : 2023
The number of days in February is 28

Enter the Month name : February
Enter the year : 2024
The number of days in February is 29
'''