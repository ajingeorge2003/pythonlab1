listcolour= [["Black", "Red", "Maroon", "Yellow"],["000000", "FF0000","800000", "FFFF00"]]
result = [
    {'colorName': listcolour[0][i], 'colorCode': listcolour[1][i]}
    for i in range(len(listcolour[0]))
]
for item in result:
    print(item)
'''
{'colorName': 'Black', 'colorCode': '000000'}
{'colorName': 'Red', 'colorCode': 'FF0000'}
{'colorName': 'Maroon', 'colorCode': '800000'}
{'colorName': 'Yellow', 'colorCode': 'FFFF00'}
'''
