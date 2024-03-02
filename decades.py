age = int(input("How old are you?\n")) ## casting is similar to c# where you just wrap the expression in a call to int() or str()

decades = age // 10 ## If you use two / instead of one, you get a whole number divison. So you do not need to cast to int explicitly.
years = age % 10

print("You are " + str(decades) + " decades and " + str(years) + " years old")