# Python Calulator

while True:
    operator = input("Enter an operator (+ - * /): ")
    if operator in ["+", "-", "*", "/"]:
        break
    else:
        print("Please enter in a valid operator.")

while True:
    try:
        num1 = int(input("Enter the 1st number: "))
        break
    except ValueError:
        print("Please enter in a number.")

while True:
    try:
        num2 = int(input("Enter the 2nd number: "))
        break
    except ValueError:
        print("Please enter in a number.")

# print(num1 + num2)

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    if num2 == 0:
        print("Cannot divide by zero.")
    else:
        print(num1 / num2)
