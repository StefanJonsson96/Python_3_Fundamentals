with open('someTextHere.txt') as file: ## this syntax is similar to using block in c# so u dont have to close the file in a finally block.
    for x in file:
        print(x)

text = input('What do you want to write to a file?')

with open('someTextHere.txt', 'a') as file2: ## the a argument opens the file in append mode, read is default.
    file2.write(text)