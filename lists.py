
list = []
list.append("hejsan") # append is similar to .Add in c#
list.append("hoppsan")
list.append("remove_this")
del list[2] ## if you want to remove via index and not via value, use the del keyword, otherwise call the .remove function
print(list[0] + list[1]) # getting a value from a specific index in a list is same as c#

for x in list: ## print each value in a list can be done with a for loop (foreach)
    print(x) 