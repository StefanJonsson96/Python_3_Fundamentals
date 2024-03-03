ageDictionary = { ## dictionaries are made with curly brackets
    'Stefan': 28,
    'Bosse' : 90,
    'Mimmi' : 35
}

ageDictionary['Rune'] = 50 ## you can add values to dictionaries like this
ageDictionary['Rune'] = 45 ## updating the value in a dictionary has the same syntax

print(ageDictionary.get('KEY_THAT_DOESNT_EXIST')) #the get function will return none instead of raising an error. none will evaluate to false in a boolean expression

for k, v in ageDictionary.items():
    print(k, v)


