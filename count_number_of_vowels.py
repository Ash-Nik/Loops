# Count the number of vowel in a string using a for loop.

x = input("please enter a string ")
count = 0
for i in x:
    if i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        count += 1
print("Total number of vowel in string = ", count)
