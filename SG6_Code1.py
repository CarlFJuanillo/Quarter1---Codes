# This program takes three numbers as input from the user,

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# calculates their sum, and prints the result rounded to two decimal places.

sum = num1 + num2 + num3

# Finally, it prints the rounded sum.

print("The sum of the three numbers is: {:.2f}".format(sum))
