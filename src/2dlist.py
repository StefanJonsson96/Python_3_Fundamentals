_2dlist = [
    ['Egg Sandwich', 'Bagel', 'Coffee'],
    ['BLT', 'PB&J', 'Turkey Sandwich'],
    ['Soup', 'Salad', 'Spaghetti', 'Taco']
]

print(_2dlist[0][1]) ## how to get inner item in 2d list

dictList = { 
    'Breakfast': _2dlist[0],
    'Lunch': _2dlist[1],
    'Dinner': _2dlist[2]
}

for name, menu in dictList.items(): ## dictionary.items() is used when you need both the key and the value, otherwise a for loop just gets the keys
    print(name, ':', menu) 