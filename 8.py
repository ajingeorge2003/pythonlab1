people = [
    {"name": "John Doe", "age": 30, "blood_group": "A+"},
    {"name": "Jane Smith", "age": 25, "blood_group": "B-"},
    {"name": "Emily Davis", "age": 40, "blood_group": "O+"},
    {"name": "Michael Brown", "age": 35, "blood_group": "AB-"},
    {"name": "William Johnson", "age": 28, "blood_group": "A-"},
    {"name": "Emma Wilson", "age": 22, "blood_group": "B+"},
    {"name": "Oliver Martinez", "age": 33, "blood_group": "O-"},
    {"name": "Sophia Anderson", "age": 27, "blood_group": "AB+"},
    {"name": "James Thomas", "age": 45, "blood_group": "A+"},
    {"name": "Isabella Lee", "age": 38, "blood_group": "B-"}
]

for person in people:
    print(f"Name : {person['name']}")
    print(f"Age : {person['age']}")
    print(f"Blood Group : {person['blood_group']}")
    print("-"*30)

'''
Name : John Doe
Age : 30
Blood Group : A+
------------------------------
Name : Jane Smith
Age : 25
Blood Group : B-
------------------------------
Name : Emily Davis
Age : 40
Blood Group : O+
------------------------------
Name : Michael Brown
Age : 35
Blood Group : AB-
------------------------------
Name : William Johnson
Age : 28
Blood Group : A-
------------------------------
Name : Emma Wilson
Age : 22
Blood Group : B+
------------------------------
Name : Oliver Martinez
Age : 33
Blood Group : O-
------------------------------
Name : Sophia Anderson
Age : 27
Blood Group : AB+
------------------------------
Name : James Thomas
Age : 45
Blood Group : A+
------------------------------
Name : Isabella Lee
Age : 38
Blood Group : B-
------------------------------
'''