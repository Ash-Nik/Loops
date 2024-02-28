# Calculate the factorial of a number using a for loop.

x = int(input("Please enter the number : "))
facto = 1
for i in range(1, x + 1):
    facto *= i
print("Factorial of the number = ", facto)
